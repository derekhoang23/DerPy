from django.conf import settings
from django.db import models
from reddit.utils.validators import validate_content
# Create your models here.



class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	user_comment = models.CharField(max_length=140, validators=[validate_content])
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user_comment)


class Stuff(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)
	quantity = models.IntegerField(default=0, blank=True)

