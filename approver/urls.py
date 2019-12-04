from django.conf.urls import url
import approver.views

urlpatterns = [
    url(r'^$', approver.views.listTweets),
    url(r'^review/(?P<tweet_id>\d+)$', approver.views.reviewTweet),
]
