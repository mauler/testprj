from unittest import TestCase

from tmw.helpers import avg


class HelpersTestCase(TestCase):

    def test_avg(self):
        """ Test average calls """
        # Normal use
        self.assertEqual(avg([1, 2.5]), 1.75)

        # Empty sequences should return 0
        self.assertEqual(avg([]), 0)
