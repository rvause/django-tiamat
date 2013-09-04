import json

from django.http import HttpResponse


def as_json(func):
    """
    Decorator that takes context and returns a HttpResponse with JSON.
    """
    def decorator(request, *ar, **kw):
        output = func(request, *ar, **kw)
        return HttpResponse(json.dumps(output), 'application/json')
    return decorator


def as_jsonp(functionCallKey='callback'):
    """
    Decorator that takes context and returns a HttpResponse with JSONP.
    """
    def decorator(func):
        def wrapper(request, *ar, **kw):
            output = func(request, *ar, **kw)
            return HttpResponse(
                "%s(%s)" % (request.GET.get(functionCallKey, functionCallKey),
                            json.dumps(output)),
                'application/json'
            )
        return wrapper
    return decorator
