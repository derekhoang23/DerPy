from django.conf import settings
from django.db import models
from reddit.utils.validators import validate_content
from reddit.models.subreddit import SubredditContent
# Create your models here.



class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	user_comment = models.CharField(max_length=140, validators=[validate_content])
	subreddit_content =  models.ForeignKey(SubredditContent, null=True, blank=True, related_name='comment', on_delete=models.CASCADE)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user_comment)


class Stuff(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)
	quantity = models.IntegerField(default=0, blank=True)



# class Album(models.Model):
#     album_name = models.CharField(max_length=100)
#     artist = models.CharField(max_length=100)

# class Track(models.Model):
#     album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
#     order = models.IntegerField()
#     title = models.CharField(max_length=100)
#     duration = models.IntegerField()

    # class Meta:
    #     unique_together = ('album', 'order')
    #     ordering = ['order']

    # def __unicode__(self):
    #     return '%d: %s' % (self.order, self.title)