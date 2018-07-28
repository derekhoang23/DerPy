from rest_framework import serializers
from reddit.models.subreddit import Subreddit, SubredditContent

class SubredditSerializer(serializers.ModelSerializer):
	subreddit_content = serializers.PrimaryKeyRelatedField(many=True, queryset=SubredditContent.objects.all())
	class Meta:
			model = Subreddit
			fields = ('name', 'id', 'subreddit_content', )

class SubredditContentDetailSerializer(serializers.ModelSerializer):
	subreddit_content_detail = serializers.PrimaryKeyRelatedField(many=True, queryset=SubredditContent.objects.all())
	class Meta:
			model = Subreddit
			fields = ('name', 'id', 'subreddit_content', )