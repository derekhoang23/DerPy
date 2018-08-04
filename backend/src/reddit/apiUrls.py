from django.conf.urls import url, include
from reddit.controllers.subreddit import SubredditContentView, SubredditView, SubredditContentDetailView
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from reddit.controllers.comment import CommentController



router = DefaultRouter()
router.register(r'subreddit_content/(?P<subreddit>[a-zA-Z]+)/(?P<subreddit_id>\d+)', SubredditContentView, base_name="subreddit_content_detail_view")
router.register(r'subreddit_content', SubredditContentDetailView, base_name='subreddit_content_list')
router.register(r'content_list', SubredditContentView, base_name='content_list')
router.register(r'comments', CommentController, base_name='comment')
router.register(r'subreddit_list', SubredditView, base_name='subreddit')
urlpatterns = [
    # url(r'^subreddit_content/(?P<subreddit>[^[A-z]+])/(?P<pk>\d+)/$', SubredditContentDetail.as_view({'get': 'retrieve'})),
    url(r'^', include(router.urls)),
]

