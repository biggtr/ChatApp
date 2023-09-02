from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import ChatRoom, Message
from django.http import Http404

# Create your views here.


def ChatRoomsList(request):
    chat_rooms = ChatRoom.objects.all()

    if not chat_rooms.exists():
        raise Http404("There are no lists in available")
    return render(request, "home.html", context={"chat_rooms": chat_rooms})


def ChatRoomDetail(request, chat_id):
    chat = get_object_or_404(ChatRoom, pk=chat_id)
    messages = get_list_or_404(Message, chat_room=chat)
    return render(
        request,
        "chat_room_detail.html",
        context={"chat": chat, "messages": messages},
    )
