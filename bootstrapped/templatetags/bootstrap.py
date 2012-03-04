from django import template
from django.conf import settings

register = template.Library()

SCRIPT_TAG = '<script src="%sjs/bootstrap-%s.js" type="text/javascript"></script>'

class BootstrapJSNode(template.Node):

    def __init__(self, args):
        self.args = set(args)

    def render_all_scripts(self):
        results = [
            SCRIPT_TAG % (settings.STATIC_URL, 'transition'),       
            SCRIPT_TAG % (settings.STATIC_URL, 'alert'),
            SCRIPT_TAG % (settings.STATIC_URL, 'dropdown'),
            SCRIPT_TAG % (settings.STATIC_URL, 'button'),
            SCRIPT_TAG % (settings.STATIC_URL, 'modal'),
            SCRIPT_TAG % (settings.STATIC_URL, 'popover'),
            SCRIPT_TAG % (settings.STATIC_URL, 'scrollspy'),
            SCRIPT_TAG % (settings.STATIC_URL, 'tab'),
            SCRIPT_TAG % (settings.STATIC_URL, 'tooltip'),
            SCRIPT_TAG % (settings.STATIC_URL, 'collapse'),
            SCRIPT_TAG % (settings.STATIC_URL, 'carousel'),
            SCRIPT_TAG % (settings.STATIC_URL, 'typeahead'),
        ]
        return '\n'.join(results)

    def render(self, context):
        if 'all' in self.args:
            return self.render_all_scripts()
        else:
            tags = [SCRIPT_TAG % (settings.STATIC_URL,tag) for tag in self.args]
            return '\n'.join(tags)

@register.simple_tag
def bootstrap_css():
    if settings.TEMPLATE_DEBUG:
        return '<link rel="stylesheet" type="text/css" href="%scss/bootstrap.css">' % settings.STATIC_URL
    else:
        return '<link rel="stylesheet" type="text/css" href="%scss/bootstrap.min.css">' % settings.STATIC_URL

@register.simple_tag
def bootstrap_responsive_css():
    if settings.TEMPLATE_DEBUG:
        return '<link rel="stylesheet" type="text/css" href="%scss/bootstrap-responsive.css">' % settings.STATIC_URL
    else:
        return '<link rel="stylesheet" type="text/css" href="%scss/bootstrap-responsive.min.css">' % settings.STATIC_URL

@register.tag(name='bootstrap_js')
def do_bootstrap_js(parser, token):
    print '\n'.join(token.split_contents())
    return BootstrapJSNode(token.split_contents()[1:])