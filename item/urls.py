from django.urls import path
from . import views

# define a namespace
app_name = 'item'

urlpatterns = [
    path('<int:id>/',views.detail, name='detail'),
]
