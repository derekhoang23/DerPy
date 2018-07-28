from rest_framework import generics, viewsets
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.permissions import AllowAny
from reddit.models.comment import Comment
from reddit.utils.serializers.comment_serializer import CommentModelSerializer
from rest_framework.views import APIView

class CommentController(viewsets.ViewSet):
	# queryset = Comment.objects.all()
	# serializer_class = CommentModelSerializer

	# @api_view(['GET'])
	# @permission_classes([AllowAny])
	# def get_subreddit_content(request):
	# 	comment = Comment.objects.all()
	# 	return Response(data=comment, status=status.HTTP_200_OK)
	def list(self, request):
		queryset = Comment.objects.all()
		serializers = CommentModelSerializer(queryset, many=True)
		print('comment serializers ', serializers.data)
		return Response(serializers.data)

