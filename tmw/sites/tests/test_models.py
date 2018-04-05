from datetime import date

from django.db.models import ProtectedError
from django.db import IntegrityError
from django.test import TestCase

from tmw.sites.models import Site


class SiteTestCase(TestCase):

    def setUp(self):
        # insert sample data into the database
        self.demo_site = Site.objects.create(name='Demo Site')

        self.demo_site.abvalues.create(entry_date=date(2012, 12, 1),
                                       value_a=1,
                                       value_b=2)

        self.demo_site.abvalues.create(entry_date=date(2012, 12, 2),
                                       value_a=1,
                                       value_b=2)

        self.demo_site.abvalues.create(entry_date=date(2012, 12, 3),
                                       value_a=1,
                                       value_b=5)

        self.abc_site = Site.objects.create(name='ABC Site')

        self.xyz_site = Site.objects.create(name='XYZ Site')

    def test_summary_for_site_without_values_entries(self):
        """ Check the values for sites with no entries. """

        # Checks value A and B sum
        self.assertEqual(self.abc_site.get_value_a_sum(), 0)
        self.assertEqual(self.abc_site.get_value_b_sum(), 0)

        # Checks value A and B average
        self.assertEqual(self.abc_site.get_value_a_avg(), 0)
        self.assertEqual(self.abc_site.get_value_b_avg(), 0)

    def test_summary_for_site_with_entries(self):
        """ Aggregate values a and b and returns it's sum and the average. """

        # Checks value A and B sum
        self.assertEqual(self.demo_site.get_value_a_sum(), 3)
        self.assertEqual(self.demo_site.get_value_b_sum(), 9)

        # Checks value A and B average
        self.assertEqual(self.demo_site.get_value_a_avg(), 1)
        self.assertEqual(self.demo_site.get_value_b_avg(), 3)


class DatabaseIntegrityTestCase(TestCase):

    def setUp(self):
        self.demo_site = Site.objects.create(name='Demo Site')
        self.abc_site = Site.objects.create(name='ABC Site')
        self.xyz_site = Site.objects.create(name='XYZ Site')

    def test_protect_deletion_of_sites_with_entries(self):
        """ Check if the Site containings A,B values entries is protected
        against deletion. """

        # Shouldn't raise error since Demo Site doesn't have any values entries
        self.demo_site.delete()

        # Create some entries for ABC Site
        self.abc_site.abvalues.create(value_a=1,
                                      value_b=2,
                                      entry_date=date(2012, 12, 1))
        with self.assertRaises(ProtectedError):
            self.abc_site.delete()

    def test_unique_date_for_sites(self):
        """ A and B Values entry are only allowed once per day. """

        # Value from different dates
        day1 = date(2012, 12, 1)
        day2 = date(2012, 12, 2)

        self.demo_site.abvalues.create(entry_date=day1,
                                       value_a=1,
                                       value_b=2)

        self.demo_site.abvalues.create(entry_date=day2,
                                       value_a=1,
                                       value_b=2)

        # Creating A, B values entry for  a specific date in a different Site
        self.abc_site.abvalues.create(entry_date=day1,
                                      value_a=1,
                                      value_b=2)

        self.abc_site.abvalues.create(entry_date=day2,
                                      value_a=1,
                                      value_b=2)

        # Trying to create a A, B values entry for a existing date should
        # raise IntegrityError
        with self.assertRaises(IntegrityError):
            self.abc_site.abvalues.create(entry_date=day2,
                                          value_a=1,
                                          value_b=2)
