from django.urls import path

from tmw.sites import views


urlpatterns = [
    path(r'', views.SiteList.as_view(), name='site_list'),
]
