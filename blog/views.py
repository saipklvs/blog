# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Sai',
        'title':'Blog Post'
    }, 
    {
        'author':'Sai',
        'title':'Blog Post 2'
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

