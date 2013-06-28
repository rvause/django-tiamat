from django.db import models

from tiamat.models import SlugMixin, GenericManager


class SlugTest(SlugMixin, models.Model):
    make_slug_from = 'name'

    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'tests'


class GMTest(models.Model):
    name = models.CharField(max_length=100)

    objects = models.Manager()
    test_objects = GenericManager(name__istartswith='test')

    class Meta:
        app_label = 'tests'
