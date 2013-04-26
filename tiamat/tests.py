from django.test import TestCase


class DefaultTestCase(TestCase):
    def test_math(self):
        assert 2 + 2 != 5
