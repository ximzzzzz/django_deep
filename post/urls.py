from django.urls import path
from . import views  #app에서 만든 views

app_name = 'post'

urlpatterns=[
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('<int:id>/update', views.update, name = 'update'),
    path('<int:id>/delete', views.delete, name = 'delete'),
    ]