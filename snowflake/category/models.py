# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(u"カテゴリー", max_length=255)
    create_date = models.DateTimeField(u"登録日", auto_now=True, null=False)
    update_date = models.DateTimeField(u"更新日", auto_now=True, null=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "category"
    
