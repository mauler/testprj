from datetime import date

from django.template import defaultfilters
from django.test import TestCase, RequestFactory

from tmw.sites.models import Site
from tmw.sites.views import SiteList, SiteDetail


class ViewsTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        # insert sample data into database
        self.demo_site = Site.objects.create(name='Demo Site')
        self.abc_site = Site.objects.create(name='ABC Site')
        self.xyz_site = Site.objects.create(name='XYZ Site')

    def test_site_list(self):
        """ Ensure all sites names are listed on the html/content returned by the
        view. """

        request = self.factory.get('/')
        response = SiteList.as_view()(request)
        response.render()

        content = response.content.decode()

        # Check if each site name is on the body
        self.assertIn(self.demo_site.name, content)
        self.assertIn(self.abc_site.name, content)
        self.assertIn(self.xyz_site.name, content)

    def test_values_entry_list(self):
        """ Ensure all A, values entries are listed on site details. """

        # Create some entries
        entry1 =  self.demo_site.valuesentry_set.create(
            entry_date=date(2012, 12, 1),
            value_a=123,
            value_b=321)

        entry2 =  self.demo_site.valuesentry_set.create(
            entry_date=date(2012, 12, 2),
            value_a=789,
            value_b=987)

        entry3 =  self.demo_site.valuesentry_set.create(
            entry_date=date(2012, 12, 3),
            value_a=456,
            value_b=654)

        request = self.factory.get('/sites/{}'.format(self.demo_site.pk))
        response = SiteDetail.as_view()(request, pk=self.demo_site.pk)
        response.render()

        content = response.content.decode()

        # Check if A,B values entry #1 is on the body.
        self.assertIn(defaultfilters.date(entry1.entry_date), content)
        self.assertIn(defaultfilters.floatformat(entry1.value_a), content)
        self.assertIn(defaultfilters.floatformat(entry1.value_b), content)

        # Check if A,B values entry #2 is on the body.
        self.assertIn(defaultfilters.date(entry2.entry_date), content)
        self.assertIn(defaultfilters.floatformat(entry2.value_a), content)
        self.assertIn(defaultfilters.floatformat(entry2.value_b), content)

        # Check if A,B values entry #3 is on the body.
        self.assertIn(defaultfilters.date(entry3.entry_date), content)
        self.assertIn(defaultfilters.floatformat(entry3.value_a), content)
        self.assertIn(defaultfilters.floatformat(entry3.value_b), content)
