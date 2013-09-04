from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def page_objects(qs, by, page=None):
    """
    Takes a queryset and the number to paginate by along with the optional
    page argument and returns the results paginated using Django's paginator
    module.
    """
    paginator = Paginator(qs, by)
    page = page or 1
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page
