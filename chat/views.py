from django.shortcuts import *
from chat.models import *
from django.http import *

from crypto_algorithms.consts import *


def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)


def send(request):
    algorithm = request.POST.get("algorithm")
    message = request.POST['message']
    print("message=", message)
    if algorithm == "Hill Cipher":
        message = encrypt_1(message)
    elif algorithm == "2Des Cipher":
        message = encrypt_2(message)
    else:
        message = "error!   "
    username = request.POST['username']
    room_id = request.POST['room_id']
    new_message = Message.objects.create(
        value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
