from django.contrib import admin

# Register your models here.

from reddit.models.subreddit import Subreddit, SubredditContent
from reddit.models.comment import Comment
# from reddit.utils.form import CommentForms

admin.site.register(Subreddit)
admin.site.register(SubredditContent)
admin.site.register(Comment)


# class CommentModelAdmin(admin.ModelAdmin):
# 	form = CommentForm

# admin.site.register(Comment, CommentModelAdmin)