# -*- coding: utf-8 -*-
from django.db import models
from category.models import Category
from users.models import Users


# Create your models here.
class Receipt(models.Model):
    category = models.ForeignKey(Category)
    user = models.ForeignKey(Users)
    name = models.CharField(u"商品名", max_length=255)
    price = models.IntegerField()
    create_date = models.DateTimeField(u"登録日", auto_now=True, null=False)
    update_date = models.DateTimeField(u"更新日", auto_now=True, null=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "receipt"

    @classmethod
    def get_by_today(cls, user_id):
        '''今日の日付で取得'''
        import datetime
        now = datetime.datetime.now()
        start = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
        end = datetime.datetime(now.year, now.month, now.day, 23, 59, 59)
        try:
            r = Receipt.objects.select_related().\
              filter(user_id=user_id, create_date__range=(start, end))
        except:
            r = None

        return r
            
    @classmethod
    def get_by_create_date(cls, user_id, start_date, end_date):
        '''日付で取得'''
        try:
            r = Receipt.objects.select_related().filter(user_id=user_id, create_date__range=(start_date, end_date))
        except:
            r = None

        return r

    @classmethod
    def register(cls, category_id, user_id, name, price):
        try:
            r = Receipt.objects.create(category_id=category_id, user_id=user_id, name=name, price=price)
        except:
            r = None

        return r



        
    
