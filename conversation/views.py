from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from .models import Conversation, ConversationMessage
from .forms import ConversationMessageForm
# Create your views here.

# when the user clicks contect_seller, this function is called
# the item_key is referencing the concerned item
@login_required
def new_conversation(request, item_pk):
    # get the item from DB 
    item = get_object_or_404(Item, pk=item_pk)
    # check if the user is not the owner of the item 
    if item.created_by == request.user :
        return redirect('dashboard:index')
    # get all conversations related to this item, where you are a member
    # check if the id of the authenticated user is one of the members of the conversation
    conversations_related_to_item = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    # if there's already a conversation redirect user to it 
    if conversations_related_to_item :
        return redirect('conversation:messages', conversation_id = conversations_related_to_item.first().id)
    
    # check if form has been submitted 
    if request.method == 'POST' and not(conversations_related_to_item) :
        form = ConversationMessageForm(request.POST)
        if form.is_valid() :
            # we create a new conversation 
            conversation = Conversation.objects.create(item=item)
            # adding the members , you and the owner of the item
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            # save the conversation 
            conversation.save()
            # create the conversation message 
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user 
            conversation_message.save()

            # redirect back to the item 
            return redirect('item:detail', id=item_pk)
    else :
        form = ConversationMessageForm()
    
    return render(request,'conversation/new.html',{'form' : form})

# this function should list all conversations for a user 
@login_required 
def inbox(request) :
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    return render(request, 'conversation/inbox.html', {
        'conversations' : conversations,
    })

# get messages for a specific conversation
@login_required
def messages(request, conversation_id) :
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=conversation_id)

    if request.method == 'POST' :
        form = ConversationMessageForm(request.POST)
        if form.is_valid() :
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            # update the conversation data
            conversation.save()
            # redirect the user back to the conversation page 
            return redirect('conversation:messages', conversation_id=conversation_id)
    else :
        form = ConversationMessageForm()

    return render(request, 'conversation/messages.html',{
        'conversation' : conversation,
        'form' : form,
    })
