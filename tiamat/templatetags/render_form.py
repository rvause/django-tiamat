from django import template


register = template.Library()


@register.simple_tag
def render_form(form):
    """
    Render a form quickly using a generic template

    Usage:
        <form>{% csrf_token %}
        {% render_form form %}
        <input type="submit>
        </form>
    """
    t = template.loader.get_template('tiamat/_form.html')
    return t.render(template.Context({'form': form}))
