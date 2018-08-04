from rest_framework import serializers
from reddit.models.subreddit import Subreddit, SubredditContent
from reddit.models.comment import Comment
from reddit.utils.serializers.comment_serializer import CommentModelSerializer

class SubredditSerializer(serializers.ModelSerializer):
	subreddit_content = serializers.PrimaryKeyRelatedField(many=True, queryset=SubredditContent.objects.all())
	class Meta:
			model = Subreddit
			fields = ('id', 'name', 'subreddit_content')

class SubredditContentDetailSerializer(serializers.ModelSerializer):
	comment = CommentModelSerializer(many=True)
	class Meta:
			model = SubredditContent
			fields = ('id', 'subreddit', 'title', 'comment')
			depth = 1

	# def create(self, validated_data):
	# 	comments_data = validated_data.pop('comment')
	# 	subreddit_content = SubredditContent.objects.create(**validated_data)
	# 	for comment_data in comments_data:
	# 		Comment.objects.create(subreddit_content=subreddit_content, **comment_data)
	# 	return subreddit_content
