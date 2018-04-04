from django.db import models

from tmw.fields import ValueField
from tmw.sites.managers import SiteManager


class Site(models.Model):
    """ Hold Site basic information. """
    objects = SiteManager()
    name = models.CharField(max_length=20)

    def get_value_a_avg(self):
        """ Returns the average of A values from the site

        :returns: Decimal
        """
        avalues = []
        for valuesentry in self.valuesentry_set.all():
            avalues.append(valuesentry.value_a)

        # Check for zero division error
        if not avalues:
            return 0
        else:
            return sum(avalues) / len(avalues)

    def get_value_b_avg(self):
        """ Returns the average of B values from the site

        :returns: Decimal
        """
        bvalues = []
        for valuesentry in self.valuesentry_set.all():
            bvalues.append(valuesentry.value_b)

        # Check for zero division error
        if not bvalues:
            return 0
        else:
            return sum(bvalues) / len(bvalues)

    def get_value_a_sum(self):
        """ Returns the sum of A values from the site

        :returns: Decimal
        """
        avalues = []
        for valuesentry in self.valuesentry_set.all():
            avalues.append(valuesentry.value_a)
        return sum(avalues)

    def get_value_b_sum(self):
        """ Returns the sum of B values from the site

        :returns: Decimal
        """
        bvalues = []
        for valuesentry in self.valuesentry_set.all():
            bvalues.append(valuesentry.value_b)
        return sum(bvalues)


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
