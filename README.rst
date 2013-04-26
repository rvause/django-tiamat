=============
django-tiamat
=============

A collection of utilities to help ...Farm


Installation
============

Add to your Python path or ``setup.py install`` and add ``'tiamat'`` to your
``INSTALLED_APPS`` setting.


Usage
=====

This is intended for general use in any project to save time writing helpers
that are common to most projects.

View Decorators
'''''''''''''''


``as_json`` will return a JSON response::

    from tiamat.decorators import as_json

    @as_json
    def some_view(request):
        #do something
        return {'key': 'value'}


``as_html`` acts much like Django's render shortcut but as a decorator::

    from tiamat.decorators import as_html

    @as_html('myapp/index.html')
    def some_view(request):
        return {'some': 'value'}


Generic Manager
'''''''''''''''

A simple way to add a manager that overrides the queryset returned.

So this::

    class SomeManager(models.Manager):
        def get_query_set(self):
            return super(SomeManager, self).get_query_set().filter(this=that)


    class SomeModel(models.Model):
        # define the model
        objects = models.Manager()
        custom_objects = SomeManager()


Becomes this::

    from tiamat.models import GenericManager

    class SomeModel(models.Model):
        # define the model
        objects = models.Manager()
        custom_objects = GenericManager(this=that)


Pagination Helper
'''''''''''''''''

A simple way to handle pagination of your querysets::

    from tiamat.paginate import page_objects

    page = page_objects(Something.objects.all(), 25, 2)

Where ``25`` is objects per page and ``2`` is the current page number


ID Encoder
''''''''''

This is a good when you are using IDs in your urls. An example would be a link
generated to confirm an email address, or a link generated to reset a user's
password.

Make sure you set the setting ``URL_ENCODER_KEY`` to something different than
your ``SECRET_KEY`` then you can::

    from tiamat.urlencoder import encoder

    encoder.encode_id(id)
    encoder.decode_id(identifier_string)


BaseView
''''''''

Provides a simple interface for views that saves you from doing ugly things
like this::

    def some_view(request):
        if request.method == 'POST':
            # something
        else:
            # something else

It instead lets you make a view like this::

    from tiamat.views import BaseView

    class SomeView(BaseView):
        allowed_methods = ['get', 'post']

        def get(self, request, *ar, **kw):
            # something

        def post(self, request, *ar, **kw):
            # something else


Template Tags
'''''''''''''

Since the markdown tags were removed from django the ``markdown`` filter is
handy if you wish to use Markdown to apply to input before displaying it
(such as in flatpages)::

    {% load markup_markdown %}
    {{ some_val|markdown }}


As an alternative to using ``form.as_p()`` or ``form.as_table()`` and dealing
with that you can define a generic template for forms by overriding the
template ``tiamat/_form.html`` and using it like so::

    {% load render_form %}
    {% render_form form %}


More?
'''''

See the source code for more.


Need Help?
==========

Email: rvause@gmail.com

Bitbucket: https://bitbucket.org/wearefarm/django-tiamat
