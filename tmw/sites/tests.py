from datetime import date

from django.db.models import ProtectedError
from django.db import IntegrityError
from django.test import TestCase

from tmw.sites.models import Site


class ModelsTestCase(TestCase):

    def setUp(self):
        self.demo_site = Site.objects.create(name='Demo Site')
        self.abc_site = Site.objects.create(name='ABC Site')
        self.xyz_site = Site.objects.create(name='XYZ Site')

    def test_protect_deletion_of_sites_with_entries(self):
        """ Check is the Site containings values entries are protected against
        deletion. """

        # Shouldn't raise error since Demo Site doesn't have any values entries
        self.demo_site.delete()

        # Create some entries for ABC Site
        self.abc_site.valuesentry_set.create(value_a=1,
                                             value_b=2,
                                             entry_date=date(2012, 12, 1))
        with self.assertRaises(ProtectedError):
            self.abc_site.delete()

    def test_unique_date_for_sites(self):
        """ A and B Values entry are only allowed once per day. """

        # Value from different dates
        day1 = date(2012, 12, 1)
        day2 = date(2012, 12, 2)

        self.demo_site.valuesentry_set.create(entry_date=day1,
                                              value_a=1,
                                              value_b=2)

        self.demo_site.valuesentry_set.create(entry_date=day2,
                                              value_a=1,
                                              value_b=2)

        # Creating A, B values entry for  a specific date in a different Site
        self.abc_site.valuesentry_set.create(entry_date=day1,
                                             value_a=1,
                                             value_b=2)

        self.abc_site.valuesentry_set.create(entry_date=day2,
                                             value_a=1,
                                             value_b=2)

        # Trying to create a A, B values entry for a existing date should
        # raise IntegrityError
        with self.assertRaises(IntegrityError):
            self.abc_site.valuesentry_set.create(entry_date=day2,
                                                 value_a=1,
                                                 value_b=2)
