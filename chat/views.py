from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.urls import reverse
from .models import ChatRoom, Message
from django.http import Http404
from .forms import MessageForm

# Create your views here.


def ChatRoomsList(request):
    chat_rooms = ChatRoom.objects.all()

    if not chat_rooms.exists():
        raise Http404("There are no lists in available")
    return render(request, "home.html", context={"chat_rooms": chat_rooms})


def ChatRoomDetail(request, chat_id):
    chat = get_object_or_404(ChatRoom, pk=chat_id)
    messages = get_list_or_404(Message, chat_room=chat)
    form = MessageForm()
    if request.method == "POST":
        return SendMessageView(request, chat, form)

    return render(
        request,
        "chat_room_detail.html",
        context={"chat": chat, "messages": messages, "form": form},
    )


def SendMessageView(request, chat, form):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.chat_room = chat
            user.sender = request.user
            user.save()
            return redirect("chat_room-detail", chat_id=chat.pk)
    else:
        form = MessageForm()
    return render(request, "chat_room_detail.html", context={"form": form})


def EditMessageView(request, chat_id):
    pass


def DeleteMessageView(request, chat_id):
    pass
