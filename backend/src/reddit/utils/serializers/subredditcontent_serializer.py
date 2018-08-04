from rest_framework import serializers
from reddit.models.subreddit import SubredditContent
from reddit.utils.serializers.comment_serializer import CommentModelSerializer
from reddit.utils.serializers.subreddit_serializer import SubredditSerializer

class SubredditContentSerializer(serializers.HyperlinkedModelSerializer):
	subreddit = SubredditSerializer()
	# comment = CommentModelSerializer()
	class Meta:
		model = SubredditContent
		fields = ('id', 'title', 'subreddit')

