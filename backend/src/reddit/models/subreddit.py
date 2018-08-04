from django.db import models
from reddit.utils.validators import validate_content
# from reddit.models.comment import Comment
# from reddit.models.subreddit_content import SubredditContent



class Subreddit(models.Model):
	name = models.CharField(max_length=50, validators=[validate_content])
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.name)


class SubredditContent(models.Model):
	subreddit = models.ForeignKey(Subreddit, null=True, related_name='subreddit_content')
	title = models.CharField(max_length=150, validators=[validate_content])
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.title)