from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

# define a spacename 
app_name = 'market'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name ='market/login.html' ,authentication_form=LoginForm), name='login'),
]
