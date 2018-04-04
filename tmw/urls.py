from django.urls import include, path


urlpatterns = [
    path('', include('tmw.sites.urls')),
]
