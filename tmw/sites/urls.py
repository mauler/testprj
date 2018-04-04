from django.urls import path

from tmw.sites import views


urlpatterns = [

    path('sites/<int:pk>/',
         views.SiteDetail.as_view(),
         name='site_detail'),

    path('summary-average/',
         views.SummaryAverage.as_view(),
         name='summary_average'),

    path('summary/',
         views.Summary.as_view(),
         name='summary'),

    path('',
         views.SiteList.as_view(),
         name='site_list'),

]
