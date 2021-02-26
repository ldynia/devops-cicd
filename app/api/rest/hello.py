import json

from django.http import HttpResponse


def index(request):
    data = {'hello': 'django'}
    jd = json.dumps(data)

    return HttpResponse(jd, content_type="application/json")