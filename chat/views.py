from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
# Create your views here.


def home(request):
    return render(request, 'home.html') 


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room_details': room_details,
        'room': room
    })


def checkroom(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if not Room.objects.filter(name=room).exists():
        new_room = Room.objects.create(name=room)
        new_room.save()
    return redirect(f'/{room}/?username={username}')


def send(request):
    username = request.POST['username']
    room_id = request.POST['room_id']
    message = request.POST['message']
    if message:
        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()
        return HttpResponse('Message Sent Successfully')
    else:
        return HttpResponse('Empty')
    

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})