# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author'      :'Sai',
        'title'       :'Blog Post',
        'content'     :'First test post',
        'date_posted' :'April 01, 2020'
    }, 
    {
        'author':'Sai',
        'title':'Blog Post 2',
        'content'     :'Second test post',
        'date_posted' :'April 02, 2020'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

