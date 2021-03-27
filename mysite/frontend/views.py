from django.shortcuts import render

from api.models import Board, Pin

def get_common():
    return{
        'rooms':Board.objects.all()
    }

def home_view(requests):
    context = get_common()

    print(context)
    return render(requests, 'frontend/home.html', context)


