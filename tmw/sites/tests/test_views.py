from django.test import TestCase, RequestFactory

from tmw.sites.models import Site
from tmw.sites.views import SiteList


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

        self.assertIn(self.demo_site.name, content)
        self.assertIn(self.abc_site.name, content)
        self.assertIn(self.xyz_site.name, content)
