from rest_framework import generics, viewsets
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from rest_framework.permissions import AllowAny
from reddit.models.subreddit import SubredditContent, Subreddit
from reddit.models.comment import Comment
from reddit.utils.serializers.subredditcontent_serializer import SubredditContentSerializer
from reddit.utils.serializers.subreddit_serializer import SubredditSerializer, SubredditContentDetailSerializer
from rest_framework.views import APIView
from rest_framework.decorators import action

class SubredditContentController(viewsets.ViewSet):
	# serializer_class = SubredditContentSerializer
	# lookup_field = 'subreddit'

	def list(self, request):
		queryset = SubredditContent.objects.all();
		print('reuest ', request)
		# queryset = self.get_queryset();
		serializer = SubredditContentSerializer(queryset, many=True)
		print('serializer ', serializer.data);
		return Response(serializer.data)
	# def 
	# @permission_classes([AllowAny])
	# def get_subreddit_content(self, request):
	# 	print('req')
	# 	subreddit_content = SubredditContent.objects.all()
	# 	return Response(data=None, status=status.HTTP_200_OK)

class SubredditContentDetail(viewsets.ViewSet):
	# queryset = Subreddit.objects.all()
	# serializer_class = SubredditContentDetailSerializer

	# def get_queryset(self):
	# 	print('self ', self)
	# 	pk = self.kawrgs['pk']
	# 	subreddit = self.kawrgs['subreddit']
	# @action(methods=['get'], detail=True)
	# def get_subreddit_detail(self, request): 
	# 	print('self ', self)
	# 	print('reqeustttt', request)

	# @action(methods=['get'], detail=True)
	# def get_subreddit_contennt(self, request, subreddit=None, pk=None):
	# 	print('self ', self)
	# 	print('request', request)
	# 	print('subreddit ', subreddit)

	def retrieve(self, request, subreddit=None, pk=None):
		print('self', self)
		print('rqeuest sub', request)
		# subreddit_content_uid = self.kwargs.get(self.lookup_subreddit_content_id)
		# subreddit = self.kwargs.get(self.lookup_subreddit_content_id)
		# queryset = self.get_queryset();
		# queryset = Subreddit.objects.all()
		serializer = SubredditContentDetailSerializer(queryset, many=True)
		return Response(serializer.data)

class Subreddit(viewsets.ViewSet):
	serializer_class = SubredditSerializer

	def list(self, request, format=None):
		queryset = Subreddit.objects.all();
		serializer = SubredditSerializer(queryset)
		print('subreddit serializer ', serializer)
		return Response(data=serializer.data, status=status.HTTP_200_OK)


