#coding=utf-8
from django.contrib import admin
from poster.models import Tweet,Comment
# Register your models here.

admin.site.register(Tweet) # 第二个参数为admin.ModelAdmin子类，展示管理显示方式
admin.site.register(Comment)
