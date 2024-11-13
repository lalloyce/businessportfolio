from django.urls import path

from . import views


url patterns = [
    path ('', views.index, name = 'index')
    path('insert/', views.insert, name='insert'),
    path('insert_data/', views.insert_data, name='insert_data'),
    path('view_data/', views.view_data, name='view_data'),
]
