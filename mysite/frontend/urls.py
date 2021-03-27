from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('<int:pk>/', views.room_view, name='room'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
