from django.test import TestCase
from django.test.client import RequestFactory
from django.core.paginator import Page

from tiamat.decorators import as_json, as_jsonp
from tiamat.paginate import page_objects
from tiamat.urlencoder import encoder
from tiamat.templatetags.tiamat_tags import render_form

from .models import SlugTest, GMTest
from .forms import TestForm


class DecoratorsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_as_json(self):
        @as_json
        def as_json_view(request):
            return {'this': 'that'}
        request = self.factory.get('/as-json-view/')
        response = as_json_view(request)
        self.assertEqual(response.content, '{"this": "that"}')

    def test_as_jsonp(self):
        @as_jsonp('callback')
        def as_jsonp_view(request):
            return {'this': 'that'}
        request = self.factory.get('/as-json-view/')
        response = as_jsonp_view(request)
        self.assertEqual(response.content, 'callback({"this": "that"})')
        request = self.factory.get('/as-json-view/?callback=test')
        response = as_jsonp_view(request)
        self.assertEqual(response.content, 'test({"this": "that"})')


class SlugMixinTest(TestCase):
    def test_make_slug(self):
        slug_1 = SlugTest.objects.create(name='Test Name')
        slug_2 = SlugTest.objects.create(name='Test Name')
        self.assertEqual(slug_1.slug, 'test-name')
        self.assertEqual(slug_2.slug, 'test-name-1')

    def test_save(self):
        slug = SlugTest.objects.create(name='Test Name')
        slug.name = 'Another Name'
        slug.save()
        self.assertEqual(slug.slug, 'test-name')
        slug.save(make_slug=True)
        self.assertEqual(slug.slug, 'another-name')


class GenericManagerTest(TestCase):
    def test_filter(self):
        person_1 = GMTest.objects.create(name='Person')
        person_2 = GMTest.objects.create(name='Test Person')
        self.assertIn(person_2, GMTest.test_objects.all())
        self.assertNotIn(person_1, GMTest.test_objects.all())


class PaginateTest(TestCase):
    def test_page_objects(self):
        for i in range(10):
            GMTest.objects.create(name='Test %s' % i)
        page = page_objects(GMTest.objects.all().order_by('name'), by=5)
        self.assertTrue(isinstance(page, Page))
        self.assertEqual(page.object_list.count(), 5)


class URLEncoderTest(TestCase):
    def test_encoder(self):
        id = 9000
        encoded = encoder.encode_id(id)
        decoded = encoder.decode_id(encoded)
        self.assertEqual(id, decoded)


class TemplateTagTest(TestCase):
    def test_render_form(self):
        form = TestForm()
        html = render_form(form)
        self.assertIn('<input', html)
