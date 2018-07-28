"""derddit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
from reddit.controllers.test_get import TestGet, api_login
from rest_framework.authtoken import views as drf_views
from reddit.apiUrls import router
from rest_framework.urlpatterns import format_suffix_patterns
# SubredditContentDetail
# router = DefaultRouter()
# router.register(r'content_list', SubredditContent)
# router.register(r'comments', Comment)
# router.register(r'subreddit_list', Subreddit)
# router.register(r'(?P<slug>[-\w]+)/(?P<subreddit_id>[^/]+)', SubredditContentDetail, base_name="subreddit_content_detail")
    # url(r'^api/', include((router.urls, 'reddit.apiUrls') , namespace='reddit.apiUrls')),


urlpatterns = [
    url(r'^api/', include('reddit.apiUrls', namespace='redditApiUrls', app_name='redditApu')),
    url(r'^login/$', api_login),
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

