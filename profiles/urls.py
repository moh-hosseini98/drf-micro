from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.UserProfileAPIView.as_view()),
]