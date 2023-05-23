from django.shortcuts import render, redirect
from item.models import Item, Category
from .forms import SignUpForm
# Create your views here.

def index(request) :
    # get the last six items that are not sold 
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    # pass this data so it will be available for the view 
    return render(request, 'market/index.html', {
        'categories' : categories,
        'items' : items,
    })

def contact(request) :
    return render(request, 'market/contact.html')

# the view that renders the signup form 
def signup(request) :
    # verify if the form has been submitted 
    if request.method == 'POST' :
        # create a new instance of the form and pass to it all the information from form submissiom
        form = SignUpForm(request.POST)
        # check if it's valid 
        if form.is_valid():
            # create the user in database
            form.save()
            # redirect to login page 
            return redirect('/login/')
    else :
        # instantiate the empty form and render it 
        form = SignUpForm()
        
    return render(request, 'market/signup.html',{'form' : form})