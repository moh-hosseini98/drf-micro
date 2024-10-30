from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,permissions

from .serializers import EventSerializer,ReplyEventSerializer
from .models import Event,Reply
from .permissions import IsOrganizerOrReadOnly


class EventAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return (
            Event.objects.select_related("organizer")
            .prefetch_related("users","likes")
            .all()
        )

    def perform_create(self,serializer):
        serializer.save(organizer=self.request.user.profile)


class RetrieveUpdateDestroyEventAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOrganizerOrReadOnly]

    def get_object(self):
        obj  = (
            Event.objects.select_related("organizer")
            .prefetch_related("users","likes")
            .get(id=self.kwargs["id"])
        )
        self.check_object_permissions(self.request,obj)
        return obj

class JoinEventAPIView(APIView):

    serializer_class = None

    def post(self,request,id):

        event = Event.objects.get(id=id)

        if event.users.filter(id=request.user.profile.id).exists():
            return Response({'msg':'You already in event!'})

        if event.organizer == request.user.profile:
            return Response({'msg':'You can not join your own event!'})    

        event.users.add(self.request.user.profile)  

        return Response({"msg":"You joined Event!"},status=status.HTTP_200_OK)

class LikeEventAPIView(APIView):

    serializer_class = None

    def post(self,request,id):
        event = Event.objects.get(id=id)

        if event.likes.filter(id=request.user.profile.id).exists():
            return Response({'msg':'You already liked event!'})

        event.likes.add(self.request.user.profile)    

        return Response({"msg":"You liked Event!"},status=status.HTTP_200_OK)


class EventMyListListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user.profile).all()
    

class ReplyEventCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReplyEventSerializer


    def get_queryset(self):
        event = Event.objects.get(id=self.kwargs["id"])
        qs = Reply.objects.filter(event=event).order_by('-created_at')

        return qs

    def perform_create(self, serializer):
        event = Event.objects.get(id=self.kwargs["id"])
        serializer.save(
            user=self.request.user.profile,
            event=event
        )