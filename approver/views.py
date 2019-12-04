from datetime import datetime

from django.contrib.auth.decorators import permission_required
from django.forms import ModelForm
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
# Create your views here.
from TweetApprover import settings
from poster.models import Tweet, Comment
from poster.views import postTweet


class ReviewForm(forms.Form): #û���κ�ʵ��ı�
    new_comment = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'cols': 50, 'row': 6}), required=False)
    APPROVAL_CHOICES = (
        ('approve', 'Approve this tweet and post it to Twitter'),
        ('reject', 'Reject this tweet and send it back to the author with your comment'))
    approval = forms.ChoiceField(choices=APPROVAL_CHOICES, widget=forms.RadioSelect)


# �ⲿ�ֶ���һ������֤


@permission_required('poster.can_approve_or_reject_tweet', login_url='/login')
def listTweets(request):
    pending_tweets = Tweet.objects.filter(state='pending').order_by('created_at')
    published_tweets = Tweet.objects.filter(state='published').order_by('-published_at')
    return render(request, 'list_tweets.html', {'pending_tweets': pending_tweets, 'published_tweets': published_tweets})


# ��һ�������г��û��������б��Լ�����״̬�������������˵�¼Ȩ�޵ģ��������ض���loginҳ��ȥ

@permission_required('poster.can_approve_or_reject_tweet', login_url='/login')
def reviewTweet(request, tweet_id):
    reviewed_tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_comment = form.cleaned_data['new_comment']  # �ӱ���ȡ�û��ύ������ ,new_commentΪReviewForm�ֶ�
            if form.cleaned_data['approval'] == 'approve':
                # publish_tweet(review_tweet)
                #sendApprovalEmail(reviewed_tweet, new_comment)
                reviewed_tweet.published_at = datetime.now()
                reviewed_tweet.state = 'published'
            else:
                #reverse(postTweet, args=[reviewed_tweet.id]) ���Ի�ȡ����Ӧ����ַ
                link = request.build_absolute_uri(reverse(postTweet, args=[reviewed_tweet.id]))  # ��ȡ�༭��������
                #sendRejectionEmail(reviewed_tweet, new_comment, link)
                reviewed_tweet.state = 'rejected'
            reviewed_tweet.save()
            if new_comment:
                c = Comment(tweet=reviewed_tweet, text=new_comment)
                c.save()
            return HttpResponseRedirect('/approve/')
    else:
        form = ReviewForm()
    return render(request, 'review_tweet.html',
                  {'form': form, 'tweet': reviewed_tweet, 'comments': reviewed_tweet.comment_set.all()})


def sendApprovalEmail(tweet, new_comment):
    body = ['Your tweet (%r) was approved & published on Twitter.' % tweet.text]
    if new_comment:
        body.append( 'The reviewer gave this feedback: %r' % new_comment)
    send_mail('Tweet Published', '%s\r\n' % (''.join(body)), settings.EMAIL_FROM, [tweet.author_email])


def sendRejectionEmail(tweet, new_comment, link):
    body = ['Your tweet(%r) was rejected.' % tweet.text]
    if new_comment:
        body.append('The reviewer gave this feedback; %r' % new_comment)
    body.append('To edit your proposed tweet, go to %s' % link)
    send_mail('Tweet rejected', '%s\r\n' % (''.join(body)), settings.EMAIL_FROM, [tweet.author_email])
