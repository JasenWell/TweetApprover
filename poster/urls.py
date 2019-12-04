# coding=utf-8


from django.conf.urls import url, include
from poster.views import *


urlpatterns = [
    url(r'^$',postTweet,name='postTweet'),
    url(r'^thankyou',thankYou,name='thankYou'),
    url(r'^edit/(?P<tweet_id>\d+)$',postTweet),
]
