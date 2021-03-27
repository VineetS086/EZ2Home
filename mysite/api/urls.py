from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path('', views.BoardList.as_view()),
    path('<int:pk>/', views.BoardDetail.as_view()),

])

