from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q 
from .models import Item, Category
from .forms import NewItemForm, EditItemForm
# Create your views here.

# the corrsponding view to when the user wants to broese items
def items(request):
   query = request.GET.get('query','')
   categorie = request.GET.get('category', 0)
   items = Item.objects.filter(is_sold=False)
   categories = Category.objects.all()

   if categorie :
      items = items.filter(category_id = categorie)

   # if the query param in get is set
   if query :
      #filter items based on those who have name or description containing the query and insensitive
      items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))



   return render(request, 'item/browse.html',{
      'items' : items,
      'query' : query,
      'categories' : categories,
      'categorie_id' : int(categorie)
   })




# this view corresponds to displaying detail about a given item nased on his id
def detail(request, id) :
    # get the item for the given id 
    item = get_object_or_404(Item, pk=id)
    related_items = Item.objects.filter(category = item.category, is_sold=False).exclude(pk=id)[0:3]
    return render(request,'item/detail.html',
                  {
                      'item' : item,
                      'related_items' : related_items,
                    })

# the view for creating a new item
@login_required
def new(request):
    # check if the form is submitted 
    if request.method == 'POST' :
      # instantitate the form object with all data submitted in post and all files
      form = NewItemForm(request.POST, request.FILES) 
      # check if the form is valid 
      if form.is_valid():
        # the created_by field is not yet added so we don't save it to db
        # this is why commit=False 
        # create object item without saving it
        item = form.save(commit=False)
        item.created_by = request.user
        item.save()
        # redirect the user to the detail page of the new created item 
        return redirect('item:detail', id=item.id)
    else :
      # instantiate the form 
      form = NewItemForm()

    return render(request,'item/form.html',{
        'form' : form,
        'title' : 'Add New Item',
    })

@login_required
def delete(request, pk) :
    # get the item to delete 
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required 
def edit(request, id):
  #get the item to edit
  item = get_object_or_404(Item, pk=id, created_by=request.user)   
  if request.method == 'POST':
     form = EditItemForm(request.POST, request.FILES, instance=item)
     if form.is_valid():
        form.save()
        return redirect('item:detail', id=item.id)
  else :
     # the form must be prefilled with data of the item to update
     form = EditItemForm(instance=item)
  
  return render(request, 'item/form.html',{
     'form' : form,
     'title' : "Edit Item"
  })

