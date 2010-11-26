# Create your views here.
from django.http import HttpResponse
from territorios.models import Departamento
from vectorformats.Formats import Django, GeoJSON


def departamentos(request):
    qs = Departamento.objects.all()
    djf = Django.Django(geodjango="geom", properties=['nombre'])
    geoj = GeoJSON.GeoJSON()
    data = geoj.encode(djf.decode(qs))
    return HttpResponse(data)
