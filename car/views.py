from django.views.generic import ListView
from django.db.models import Q
from .models import Car


class CarListView(ListView):
    model = Car
    context_object_name = 'car_list'
    template_name = 'index.html'


class CarLSearchView(ListView):
    model = Car
    context_object_name = 'car_list'
    template_name = 'index.html'

    def get_queryset(self):
        car_make = self.request.GET.get('make')
        car_model = self.request.GET.get('model')
        car_year = self.request.GET.get('year')
        car_transmission = self.request.GET.get('transmission')
        car_color = self.request.GET.get('color')

        return Car.objects.filter(
            Q(make__icontains=car_make) &
            Q(model__icontains=car_model) &
            Q(year__icontains=car_year) &
            Q(transmission__icontains=car_transmission) &
            Q(color__icontains=car_color)
        )
