from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
	subreddit = serializers.SerializerMethodField()
	
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'subreddit'
		]

	def get_subreddit(self, obj):
		return 0