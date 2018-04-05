from django.db.models.functions import Coalesce
from django.db.models import Manager, QuerySet, Sum, Avg


class SiteManager(Manager):
    """ Manager for Site model. """

    def get_queryset(self):
        return SiteManagerQuerySet(self.model, using=self._db)

    def summary(self, *ar, **kw):
        return self.get_queryset().summary(*ar, **kw)


class SiteManagerQuerySet(QuerySet):
    """ ManagerQuerySet for Site model. """

    def summary(self):
        """ Summarizes A, B values entries, returning average and sum. """
        return self.annotate(
            value_a_sum=Coalesce(Sum('abvalues__value_a'), 0),
            value_b_sum=Coalesce(Sum('abvalues__value_b'), 0),
            value_a_avg=Coalesce(Avg('abvalues__value_a'), 0),
            value_b_avg=Coalesce(Avg('abvalues__value_b'), 0))
