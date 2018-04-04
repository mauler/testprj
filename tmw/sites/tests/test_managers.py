from datetime import date

from django.test import TestCase

from tmw.sites.models import Site


class ManagersTestCase(TestCase):

    def setUp(self):
        # insert sample data into the database
        self.demo_site = Site.objects.create(name='Demo Site')

        self.demo_site.valuesentry_set.create(entry_date=date(2012, 12, 1),
                                              value_a=1,
                                              value_b=2)

        self.demo_site.valuesentry_set.create(entry_date=date(2012, 12, 2),
                                              value_a=1,
                                              value_b=2)

        self.demo_site.valuesentry_set.create(entry_date=date(2012, 12, 3),
                                              value_a=1,
                                              value_b=5)

        self.abc_site = Site.objects.create(name='ABC Site')

        self.xyz_site = Site.objects.create(name='XYZ Site')

    def test_summary_for_site_without_values_entries(self):
        """ Check the values for sites with no entries. """
        abc_site = Site.objects.summary().get(pk=self.abc_site.pk)

        # Checks value A and B sum
        self.assertEqual(abc_site.value_a_sum, 0)
        self.assertEqual(abc_site.value_b_sum, 0)

        # Checks value A and B average
        self.assertEqual(abc_site.value_a_avg, 0)
        self.assertEqual(abc_site.value_b_avg, 0)

    def test_summary_for_site_with_entries(self):
        """ Aggregate values a and b and returns it sums and average. """
        demo_site = Site.objects.summary().get(pk=self.demo_site.pk)

        # Checks value A and B sum
        self.assertEqual(demo_site.value_a_sum, 3)
        self.assertEqual(demo_site.value_b_sum, 9)

        # Checks value A and B average
        self.assertEqual(demo_site.value_a_avg, 1)
        self.assertEqual(demo_site.value_b_avg, 3)
