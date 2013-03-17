# from django.core.serializers import json
from django.forms import Textarea
from django.utils.safestring import mark_safe
import json


class RedactorWidget(Textarea):
    class Media:
        css = {
            'all': ('suit-redactor/redactor/redactor.css',)
        }
        js = ('suit-redactor/redactor/redactor.min.js',)

    def __init__(self, attrs=None, editor_options=None):
        super(RedactorWidget, self).__init__(attrs)
        self.editor_options = editor_options or {}


    def render(self, name, value, attrs=None):
        output = super(RedactorWidget, self).render(name, value, attrs)
        output += mark_safe(
            '<script type="text/javascript">$("#id_%s").redactor(%s);</script>'
            % (name, json.dumps(self.editor_options)))
        return output