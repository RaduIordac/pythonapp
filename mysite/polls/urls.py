from django.urls import path
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('polls', views.index, name='index'),
    path('brrr/', views.bnew, name="new"),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
