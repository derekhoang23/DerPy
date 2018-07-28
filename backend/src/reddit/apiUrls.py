from django.conf.urls import url, include
from reddit.controllers.subreddit import SubredditContentController, Subreddit, SubredditContentDetail
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from reddit.controllers.comment import CommentController

router = DefaultRouter()
router.register(r'subreddit_content', SubredditContentDetail, base_name="subreddit_content")
router.register(r'content_list', SubredditContentController, base_name='content_list')
router.register(r'comments', CommentController, base_name='comment')
router.register(r'subreddit_list', Subreddit, base_name='subreddit')
urlpatterns = [
    # url(r'^subreddit_content/(?P<subreddit>[^[A-z]+])/(?P<pk>\d+)/get_subreddit_content/$', SubredditContentDetail.as_view()),
    url(r'^', include(router.urls)),
]

