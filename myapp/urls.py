from django.urls import path
from .views import my_view, my_text_view, CarListView

urlpatterns = [
    #path("listado/", my_view),
    path("listado/", CarListView.as_view()),
    path("detalle/<int:id>", my_text_view),
    path("marcas/<str:brand>", my_text_view)
]
