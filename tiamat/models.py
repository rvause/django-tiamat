from django.db import models


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
