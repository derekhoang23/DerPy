from rest_framework import generics, viewsets
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from rest_framework.decorators import detail_route
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from reddit.models.subreddit import SubredditContent, Subreddit
from reddit.models.comment import Comment
from reddit.utils.serializers.subredditcontent_serializer import SubredditContentSerializer
from reddit.utils.serializers.subreddit_serializer import SubredditSerializer, SubredditContentDetailSerializer
from rest_framework.views import APIView
from rest_framework.decorators import action

class SubredditContentView(viewsets.ViewSet):
	# serializer_class = SubredditContentSerializer
	# lookup_field = 'subreddit'

	def list(self, request):
		queryset = SubredditContent.objects.all();
		# queryset = self.get_queryset();
		serializer = SubredditContentSerializer(queryset, many=True)
		return Response(serializer.data)
	# def
	# @permission_classes([AllowAny])
	# def get_subreddit_content(self, request):
	# 	print('req')
	# 	subreddit_content = SubredditContent.objects.all()
	# 	return Response(data=None, status=status.HTTP_200_OK)

# from django.db.models import Q
# import operator
# class MultipleFieldLookupMixin(object):
#   def get_object(self):
#     queryset = self.get_queryset()             # Get the base queryset
#     queryset = self.filter_queryset(queryset)  # Apply any filter backends
#     filter = {}
#     for field in self.lookup_fields:
#     	print('field ', field)
#     	filter[field] = self.kwargs[field]
#     q = reduce(operator.or_, (Q(x) for x in filter.items()))
#     return get_object_or_404(queryset, q)


class SubredditContentDetailView(viewsets.ViewSet):
	queryset = SubredditContent.objects.all()

	def list(self, request):
		print('self', self)
		subreddit_name = self.kwargs.get('subreddit', None)
		subreddit_id = self.kwargs.get('subreddit_id', None)
		if subreddit_name is None and subreddit_id is None:
			queryset = SubredditContent.objects.all()
			serializer = SubredditContentDetailSerializer(queryset, many=True, context={'request': None})
			return Response(serializer.data)


class SubredditView(viewsets.ViewSet):
	def list(self, request):
		queryset = Subreddit.objects.all();
		print('query set ', queryset)
		serializer = SubredditSerializer(queryset, many=True)
		return Response(data=serializer.data, status=status.HTTP_200_OK)


