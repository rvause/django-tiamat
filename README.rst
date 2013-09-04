=============
django-tiamat
=============

A collection of utilities to help in Django Projects

|TravisButton|_


Installation
============

``pip install django-tiamat``

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


``as_jsonp`` will return a JSONP response::

    from tiamat.decorators import as_jsonp

    @as_jsonp('callback')
    def some_view(request):
        #do something
        return {'key': 'value'}


```http://.../?callback=myFunctionCall```

returns ```myFunctionCall({"foo": "1"})```


Model Mixins
''''''''''''

``SlugMixin`` will add a slug field (named slug) to your model that will be
automatically generated from a field called '``name``' on saving. If you wish
to override the default field to generate the slug from set ``make_slug_from``
on the model. See the source for more details.


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


Email
'''''

``send_async_email`` provides an easy helper to send email using a template::

    from tiamat.mail import send_async_email

    send_async_email(
        'path/to/template.html',
        {'name': 'Steve'},
        'Hello',
        [user.email for user in User.objects.all()]
    )


Template Tags
'''''''''''''

As an alternative to using ``form.as_p()`` or ``form.as_table()`` and dealing
with that you can define a generic template for forms by overriding the
template ``tiamat/_form.html`` and using it like so::

    {% load tiamat_tags %}
    {% render_form form %}


More?
'''''

See the source code for more.

Running Tests
=============

To run the tests::

    python setup.py test


Need Help?
==========

Email: rvause@gmail.com

Github: https://github.com/rvause/django-tiamat


.. |TravisButton| image:: https://travis-ci.org/rvause/django-tiamat.png?branch=master
.. _TravisButton: https://travis-ci.org/rvause/django-tiamat
