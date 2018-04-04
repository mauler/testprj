from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from tmw.sites.models import Site, ValuesEntry


class SiteList(ListView):
    model = Site


class SiteDetail(DetailView):
    model = Site
