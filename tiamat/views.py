from django.http import HttpResponse
from django.http.request import QueryDict


class HttpMethodNotAllowed(HttpResponse):
    status_code = 405


class BaseView(object):
    allowed_methods = ['get']

    def __new__(cls, *ar, **kw):
        return super(BaseView, cls).__new__(cls)(*ar, **kw)

    def __call__(self, request, *ar, **kw):
        method = request.method.lower()
        if method not in ['get', 'post']:
            setattr(request, method.upper(), QueryDict(request.body))
        if method not in self.allowed_methods:
            return HttpMethodNotAllowed('Not allowed: %s' % method.upper())
        method_call = getattr(self, method)
        return method_call(request, *ar, **kw)

    def get(self, request, *ar, **kw):
        raise NotImplementedError

    def post(self, request, *ar, **kw):
        raise NotImplementedError

    def put(self, request, *ar, **kw):
        raise NotImplementedError

    def delete(self, request, *ar, **kw):
        raise NotImplementedError
