from django.contrib.auth.models import User
from django.db import models
from item.models import Item
# Create your models here.

# model that represents a conversation in database
class Conversation(models.Model) :
    # we reference the item as an attribute for a conversation object
    # when a item is deleted all related conversations are also 
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    # the members of the conversation 
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    # every the time the object is saved, this will be automatically updated
    modified_at = models.DateTimeField(auto_now=True)

    class Meta :
        ordering = ('-modified_at',)


# model that represents a message of the conversation

class ConversationMessage(models.Model) :
    # reference the conversation to which the message belongs
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    
