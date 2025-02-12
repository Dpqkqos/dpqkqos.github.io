from django.shortcuts import render
from django.http import JsonResponse
from .models import UserState
from datetime import date

def user_state(request, chat_id):
    try:
        user_state = UserState.objects.get(chat_id=chat_id, date=date.today())
    except UserState.DoesNotExist:
        user_state = None

    return render(request, 'index.html', {'user_state' : user_state})

def save_state(request):
    if request.method == "POST":
        chat_id = request.POST.get('chat_id')
        state = request.POST.get('state')

        user_state, create = UserState.objects.update_or_create(
            chat_id=chat_id, date=date.today(), defaults={'state' : state}
        )

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})