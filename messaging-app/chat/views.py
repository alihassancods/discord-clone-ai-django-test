from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
from django.views.decorators.csrf import csrf_exempt
import json

def chatroom(request):
    return render(request, 'chat/chatroom.html')

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = Message.objects.create(
            user=data['user'],
            content=data['content']
        )
        return JsonResponse({'id': message.id, 'user': message.user, 'content': message.content})

def get_messages(request):
    messages = Message.objects.all().values('id', 'user', 'content')
    return JsonResponse(list(messages), safe=False)