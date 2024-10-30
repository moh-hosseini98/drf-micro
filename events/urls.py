from django.urls import path
from . import views


urlpatterns = [
    path('events/',views.EventAPIView.as_view()),
    path('events/<int:id>/',views.RetrieveUpdateDestroyEventAPIView.as_view()),
    path('events/<int:id>/join/',views.JoinEventAPIView.as_view()),
    path('events/<int:id>/like/',views.LikeEventAPIView.as_view()),
    path('events/<int:id>/reply/',views.ReplyEventCreateAPIView.as_view()),
    path('events/my/',views.EventMyListListAPIView.as_view()),
]
