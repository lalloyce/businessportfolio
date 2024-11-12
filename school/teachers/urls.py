from django.urls import path

from . import views
url patterns = [
    path ('', view.index, name = 'index')
    path('insert/', views.insert, name='insert'),

