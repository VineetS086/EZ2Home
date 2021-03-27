from django.http.response import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.contrib.auth import logout

from api.models import Board, Pin

def get_common():
    return{
        'rooms':Board.objects.all()
    }

def home_view(requests):
    context = get_common()

    return render(requests, 'frontend/home.html', context)

def room_view(requests, pk):
    context                 = get_common()
    context['Room']         = get_object_or_404(Board, id=pk)
    context['appliances']   = get_list_or_404(Pin, board__id=pk)

    return render(requests, 'frontend/room.html', context)


def login_view(request):
    return HttpResponse('login')


def logout_view(request):
    logout(request)
    return redirect('home')