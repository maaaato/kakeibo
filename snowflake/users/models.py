# -*- coding: utf-8 -*-
from django.db import models
from session.utile.base_utile import Session


# Create your models here.
class Users(models.Model):
    username = models.CharField(u"ユーザ名", max_length=255)
    email = models.CharField(u"メールアドレス", max_length=75)
    password = models.CharField(u"パスワード", max_length=255)
    date_joined = models.DateTimeField(u"登録日", auto_now=True, null=False)
    last_login = models.DateTimeField(u"最終ログイン日", auto_now=True, null=False)
        
    def __unicode__(self):
        return self.username

    class Meta:
        db_table = "users"

    @classmethod
    def get_user_by_id(cls, id):
        '''IDで取得'''
        try:
            m = Users.objects.get(id__exact=id)
        except:
            m = None
            
        if m:
            return m
            
        return None
    
    @classmethod
    def get_user(cls, username, password):
        '''IDとPASSをチェック'''
        try:
            m = Users.objects.get(username__exact=username)
        except:
            m = None
            
        if m:
            if m.password == password:
                return m
            
        return None
