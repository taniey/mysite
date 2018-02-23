#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from . import views

# add the label for app namespacing
app_name = 'polls'

urlpatterns = [
    # path('', views.hello_world, name='hello_world_url'),
    # path('index/', views.index, name='index_url'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail_url'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results_url'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote_url'),
    path('', views.hello_world, name='hello_world_url'),
    path('index/', views.IndexView.as_view(), name='index_url'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail_url'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results_url'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote_url'),
]
