from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from tmw.sites.models import Site, ValuesEntry


class SiteList(ListView):
    model = Site


class Summary(SiteList):
    template_name = 'sites/summary.html'

    def get_queryset(self, *ar, **kwargs):
        """ Returns all sites with summarized values. """
        qs = super().get_queryset(*ar, **kwargs)
        # Summarize the queryset
        qs = qs.summary()
        return qs


class SummaryAverage(Summary):
    template_name = 'sites/summary_average.html'


class SiteDetail(DetailView):
    model = Site
