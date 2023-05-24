from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
    path('inbox/',views.inbox, name='inbox'),
    path('messages/<int:conversation_id>/', views.messages, name='messages'),
]
