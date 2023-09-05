from django.urls import path
from .views import ChatRoomsList, ChatRoomDetail, EditMessageView, DeleteMessageView

urlpatterns = [
    path("", ChatRoomsList, name="chat_room-list"),
    path("chat/<int:chat_id>/", ChatRoomDetail, name="chat_room-detail"),
    path(
        "chat/<int:chat_id>/edit/<int:message_id>/",
        EditMessageView,
        name="edit-message",
    ),
    path(
        "chat/<int:chat_id>/delete/<int:message_id>/",
        DeleteMessageView,
        name="delete-message",
    ),
]
