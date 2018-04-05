from django.db import models

from tmw.fields import ABValueField
from tmw.helpers import avg
from tmw.sites.managers import SiteManager


class Site(models.Model):
    """ Hold Site basic information. """

    objects = SiteManager()

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_value_a_avg(self):
        """ Returns the average of A values from the site

        :returns: Decimal
        """
        return avg(self.valuesentry_set.values_list('value_a', flat=True))

    def get_value_b_avg(self):
        """ Returns the average of B values from the site

        :returns: Decimal
        """
        return avg(self.valuesentry_set.values_list('value_b', flat=True))

    def get_value_a_sum(self):
        """ Returns the sum of A values from the site

        :returns: Decimal
        """
        return sum(self.valuesentry_set.values_list('value_a', flat=True))

    def get_value_b_sum(self):
        """ Returns the sum of B values from the site

        :returns: Decimal
        """
        return sum(self.valuesentry_set.values_list('value_b', flat=True))


class ValuesEntry(models.Model):
    """ Holds A and B values entry for a Site for a specific date.

    - The entry date is unique for each Site.
    - A and B values should be a Decimal with 2 decimal places."""

    site = models.ForeignKey('Site', on_delete=models.PROTECT)

    value_a = ABValueField()

    value_b = ABValueField()

    entry_date = models.DateField()

    class Meta:
        unique_together = ('site', 'entry_date', )
