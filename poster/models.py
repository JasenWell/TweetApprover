# coding=utf-8
from django.db import models


# Create your models here.

class Tweet(models.Model):
    text = models.CharField(max_length=140)
    author_email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    STATE_CHOICE = (
        ('pending', 'pending'),
        ('published', 'published'),
        ('rejected', 'rejected')
    )

    state = models.CharField(max_length=15, choices=STATE_CHOICE)

    def __unicode__(self):  # 此方式替换admin管理该类显示方式
        return self.text

    class Meta:
        # 权限设置
        permissions = (
            ('can_approve_or_reject_tweet', 'can_approve_or_reject_tweets'),
        )


class Comment(models.Model):
    tweet = models.ForeignKey(Tweet)
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text
