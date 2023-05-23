from django.shortcuts import render, get_object_or_404
from .models import Item
# Create your views here.
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

