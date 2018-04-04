from django.db import models

from tmw.fields import ValueField
from tmw.sites.managers import SiteManager


class Site(models.Model):
    """ Hold Site basic information. """
    objects = SiteManager()
    name = models.CharField(max_length=20)


class ValuesEntry(models.Model):
    """ Holds A and B values entry for a Site for a specific date.

    - The entry date is unique for each Site.
    - A and B values should be a Decimal with 2 decimal places."""

    site = models.ForeignKey('Site', on_delete=models.PROTECT)

    value_a = ValueField()

    value_b = ValueField()

    entry_date = models.DateField()

    class Meta:
        unique_together = ('site', 'entry_date', )
