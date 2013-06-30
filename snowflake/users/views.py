# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, loader
from user.models import users

def login_index(request):

    if request.method == "POST":
        
    return render_to_response('login_index.html',c)
