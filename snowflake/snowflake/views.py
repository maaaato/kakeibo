# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from session.utile.base_utile import Session
from users.models import Users
from receipt.models import Receipt
from snowflake.decorate import login_required
from category.models import Category


@login_required
def index(request):
    """mypage"""
    user = request.user

    receipt = Receipt.get_by_today(user.pk)
    category = Category.objects.all()
    rctxt = RequestContext(request, {
        "member": user,
        "receipt": receipt,
        "category": category,
    })
    
    return render_to_response(
        'index.html', "",
        context_instance=rctxt)


def login(request):
    """ログイン"""
    user = None
    if request.method == "POST":
        if request.POST["username"] and request.POST["password"]:
            user = Users.get_user(request.POST["username"],\
                                  request.POST["password"])
            if user:
                Session.set_user_id(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        return render_to_response(
            'login_index.html', "",
            context_instance=RequestContext(request))

    return HttpResponseRedirect(reverse('login'))
