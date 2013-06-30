# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from receipt.models import Receipt
from snowflake.decorate import login_required


@login_required
def receipt_regist(request):
    """レシートの登録"""
    
    user = request.user
    category = int(request.POST["category"])
    name = request.POST["name"]
    price = int(request.POST["price"])

    r = Receipt.register(category, user.pk, name, price)

    return HttpResponseRedirect(reverse('index'))
