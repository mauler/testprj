from django.views.generic.list import ListView

from tmw.sites.models import Site


class SiteList(ListView):
    model = Site
