from django.views.generic.edit import CreateView
from rest_framework import generics, viewsets
from reddit.models.comment import Comment, Stuff
from reddit.utils.serializers.comment_serializer import CommentModelSerializer
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny


class TestGet(generics.ListAPIView):
	serializer_class = CommentModelSerializer

	def get_queryset(self):
		return Comment.objects.all()

@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
  username = request.data['username']
  password = request.data['password']
  user = authenticate(username=username, password=password)
  if user is not None:
      login(request, user)
      return Response(status=status.HTTP_200_OK)
  return Response(status=status.HTTP_400_BAD_REQUEST)


