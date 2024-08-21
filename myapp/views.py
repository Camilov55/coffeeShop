
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def my_view(request): # Vista basada en funciones 
    car_list = [
        {"title": "BMW" },
        {"title": "Mazda"}
    ]
    context = {
        "car_list": car_list
    }
    return render(request, "myFirstApp/carList.html", context)

class CarListView(TemplateView): # Vista basada en clases
    template_name = "myFirstApp/carList.html"

    def get_context_data(self):
        car_list = [
            {"title": "BMW" },
            {"title": "Mazda"}
        ]
        return {
            "car_list": car_list
        }



def my_text_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")