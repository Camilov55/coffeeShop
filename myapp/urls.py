from django.http import HttpResponse
from django.urls import path

def my_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

urlpatterns = [
    path("listado/", my_view),
    path("detalle/<int:id>", my_view),
    path("marcas/<str:brand>", my_view)
]
