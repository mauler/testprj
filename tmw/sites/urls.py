from django.urls import path

from tmw.sites import views


urlpatterns = [
    path('sites/<int:pk>/', views.SiteDetail.as_view(), name='site_detail'),
    path('', views.SiteList.as_view(), name='site_list'),
]
