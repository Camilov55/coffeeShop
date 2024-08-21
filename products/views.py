from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductFroms

# Create your views here.

class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductFroms
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)