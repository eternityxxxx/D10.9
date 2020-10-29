from django.views.generic import ListView
from .models import Car


class CarListView(ListView):
    model = Car
    context_object_name = 'car_list'
    template_name = 'index.html'
