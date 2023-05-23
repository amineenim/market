from django.urls import path

from . import views

# define a spacename 
app_name = 'market'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('signup/', views.signup, name='signup'),
]
