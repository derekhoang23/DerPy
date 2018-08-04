from rest_framework import generics, viewsets
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.permissions import AllowAny
from reddit.models.comment import Comment
from reddit.utils.serializers.comment_serializer import CommentModelSerializer
from reddit.utils.serializers.subreddit_serializer import SubredditContentDetailSerializer
from rest_framework.views import APIView
from reddit.models.subreddit import SubredditContent

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

	def create(self, request, subreddit=None, subreddit_id=None, content_id=None):
		comment = request.data.get('user_comment', None)
		user = request.data.get('user', None)
		subreddit_content_id = request.data.get('subreddit_content', None)
		comment = Comment(user=request.user,
			user_comment=comment,
			subreddit_content=SubredditContent.objects.get(pk=subreddit_content_id))
		comment.save()
		return Response(status=status.HTTP_201_CREATED)
		# queryset = SubredditContent.objects.filter(pk=content_id);
		# for items in queryset:
		# 	print('items ', items)
		# serializer = SubredditContentDetailSerializer(queryset, many=True)
		# subreddit_content = serializer.data
		# for item in subreddit_content:
		# 	subreddit_query = item.get('subreddit').get('id')
		# 	subreddit_id = int(subreddit_id)
		# 	if subreddit_query == subreddit_id:
		# 		return Response(item)

