# coding=utf-8
from django.shortcuts import render
from django import forms
from django.forms import ModelForm
from poster.models import Tweet
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.db.models import Count
from django.views.decorators.cache import cache_page


# Create your views here.


class TweetForm(ModelForm):
    class Meta:
        model = Tweet  # 对应的模型
        fields = ('text', 'author_email')  # 只从表单取这些变量
        widgets = {  # 修改组件
                      'text': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
                  },


@cache_page(15 * 60) #缓存15分钟
def postTweet(request, tweet_id=None):
    tween = None
    if tweet_id:  # 存在id，从数据库取
        tween = get_object_or_404(Tweet, id=tweet_id)
    if request.method == 'POST':
        form = TweetForm(request.POST, instance=tween)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.state = 'pending'
            new_form.save()
            # sendReviewMail()
            return HttpResponseRedirect('/post/thankyou')
    else:
        form = TweetForm(instance=tween)
    return render(request, 'post_tween.html', {'form': form})
    pass


def sendReviewMail():
    subject = 'Action required: review tweet'
    message = 'A new tween has been submitted for approval,Please review it as soon as possible'
    from_email = ''
    receive_email = ''
    send_mail(subject, message, from_email, [receive_email])


def thankYou(request):
    # aggregate这个函数是一个聚合函数，是Django内置的数据库基本操作函数，用于统计执行的结果是返回一个字典，这里返回的字典是{u’id__count’: 1}，这里我们取值就是了
    maps = Tweet.objects.filter(state='pending').aggregate(Count('id'))
    tweens_in_queen = list(maps.values())[0]
    return render(request, 'thank_you.html', {'tweens_in_queen': tweens_in_queen})
