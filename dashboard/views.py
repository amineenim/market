from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request) :
    # start by getting items of the authenticated user 
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html',{
        'items' : items
    })







