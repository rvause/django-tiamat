from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class GenericManager(models.Manager):
    """
    Filter query set by given selectors
    """
    def __init__(self, **kw):
        super(GenericManager, self).__init__()
        self.selectors = kw

    def get_query_set(self):
        return super(GenericManager, self).get_query_set().filter(
            **self.selectors
        )


class SlugMixin(models.Model):
    """
    Mixin for an auto generated slug
    """
    make_slug_from = 'name'
    slug = models.SlugField(
        _('slug'),
        unique=True,
        max_length=255,
        help_text=_('Unique identifier for use in urls')
    )

    class Meta:
        abstract = True

    def save(self, *ar, **kw):
        make_slug = kw.pop('make_slug', False)
        if not self.id or make_slug:
            self.make_slug()
        super(SlugMixin, self).save(*ar, **kw)

    def make_slug(self):
        slug = new_slug = slugify(getattr(self, self.make_slug_from))[:255 - 5]
        counter = 0
        while True:
            try:
                obj = self.__class__.objects.get(slug=new_slug)
                if obj.id == self.id:
                    break
                counter += 1
                new_slug = '%s-%d' % (slug, counter)
            except self.__class__.DoesNotExist:
                break
        self.slug = new_slug
