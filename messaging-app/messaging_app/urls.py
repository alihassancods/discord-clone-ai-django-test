from django.urls import path
from chat import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatroom/<str:room_name>/', views.chatroom, name='chatroom'),
]