"""dj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from myapp import views, account

urlpatterns = [

   # path("admin/", admin.site.urls),
path("index/", views.index),
path('home/',views.home),
path('locate/',views.locate),
path('user/add/',views.user_add),
path('user/list/',views.user_list),
path('user/delete/',views.user_delete),
path('user/<int:nid>/edit/',views.user_edit),
path('detect/add/',views.detect_add),
path('detect/list/',views.detect_list),
path('detect/delete/',views.detect_delete),
path('detect/<int:nid>/edit/',views.detect_edit),

path('tracert/list/',views.tracert_list),
path('tracert/delete/',views.tracert_delete),
path('tracert/cluster_last/',views.tracert_cluster_last),
path('tracert/cluster_last2/',views.tracert_cluster_last2),
path('register/',views.register),
path('load/',account.load),
path('logout/',account.logout),
path('local/add',views.local_add),
path('local/delete/',views.local_delete),
path('local/<int:nid>/edit/',views.local_edit),
re_path(r'^$',account.load)
]
