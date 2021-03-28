from django.http.response import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from api.models import Board, Pin

def get_common(requests):
<<<<<<< Updated upstream

=======
    if not requests.user.is_authenticated:
        return redirect('login')
>>>>>>> Stashed changes
    return{
        'rooms':Board.objects.all()
    }

def home_view(requests):
<<<<<<< Updated upstream
    if not requests.user.is_authenticated:
        return redirect('login')
=======
>>>>>>> Stashed changes
    context = get_common(requests)

    return render(requests, 'frontend/home.html', context)

def room_view(requests, pk):
<<<<<<< Updated upstream
    if not requests.user.is_authenticated:
        return redirect('login')
=======
>>>>>>> Stashed changes
    context                 = get_common(requests)
    context['Room']         = get_object_or_404(Board, id=pk)
    context['appliances']   = get_list_or_404(Pin, board__id=pk)

    return render(requests, 'frontend/room.html', context)


def login_view(requests):
    if requests.user.is_authenticated:
        return redirect('login')

    if requests.method == 'POST':
        form = AuthenticationForm(request=requests, data=requests.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(requests, user)
                messages.info(requests, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(requests, "Invalid username or password.")
        else:
            messages.error(requests, "Invalid username or password.")
    form = AuthenticationForm()

    return render(requests, 'frontend/login.html',{"form":form})


def logout_view(requests):
    logout(requests)
    return redirect('login')