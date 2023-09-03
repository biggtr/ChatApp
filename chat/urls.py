from django.urls import path
from .views import ChatRoomsList, ChatRoomDetail

urlpatterns = [
    path("", ChatRoomsList, name="chat_room-list"),
    path("chat/<int:chat_id>/", ChatRoomDetail, name="chat_room-detail"),
]
