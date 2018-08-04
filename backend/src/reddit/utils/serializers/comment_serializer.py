from rest_framework import serializers
from accounts.utils.serializers import UserDisplaySerializer
from reddit.models.comment import Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer()
	class Meta:
		model = Comment
		fields = ('id', 'user', 'user_comment')

	# def create(self, validated_data):
	# 	model_comment_data = validated_data.pop('user')
	# 	model_comment = Comment.objects.create(**validated_data)
	# 	User.objects.create(model_comment=model_comment, **model_comment_data)
	# 	return model_commen
