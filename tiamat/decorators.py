import json
from functools import wraps

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def as_json(func):
    def decorator(request, *ar, **kw):
        output = func(request, *ar, **kw)

        if not isinstance(output, dict):
            return output

        return HttpResponse(json.dumps(output), 'application/json')
    return decorator


def as_jsonp(functionCallKey='callback'):
    def decorator(func):
        def wrapper(request, *ar, **kw):
            output = func(request, *ar, **kw)

            if not isinstance(output, dict):
                return output

            return HttpResponse(
                "%s(%s)" % (request.GET.get(functionCallKey),
                            json.dumps(output)),
                'application/json'
            )
        return wrapper
    return decorator


def as_html(template_path):
    """
    Decorator with the same functionality as render_to_response has, but uses
    decorator syntax.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            output = func(request, *args, **kwargs)

            if not isinstance(output, dict):
                return output

            return render_to_response(
                template_path,
                output,
                context_instance=RequestContext(request)
            )
        return wrapper
    return decorator
