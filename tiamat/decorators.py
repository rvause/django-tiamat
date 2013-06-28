import json

from django.http import HttpResponse


def as_json(func):
    def decorator(request, *ar, **kw):
        output = func(request, *ar, **kw)
        return HttpResponse(json.dumps(output), 'application/json')
    return decorator


def as_jsonp(functionCallKey='callback'):
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
