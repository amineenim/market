from django.urls import path
from . import views

# define a namespace
app_name = 'item'

urlpatterns = [
    path('browse/', views.items, name='browse'),
    path('new/',views.new, name='newitem'),
    path('<int:id>/',views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:id>/edit/', views.edit, name='edit')
]
