from django.urls import path
from . import views
# define a spacename
app_name = 'dashboard'

urlpatterns = [
    path('',views.index, name='index'),

]
