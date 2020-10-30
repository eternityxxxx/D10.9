from django.urls import path
from .views import CarListView, CarLSearchView


urlpatterns = [
    path('list/', CarListView.as_view(), name='car_list'),
    path('search/', CarLSearchView.as_view(), name='car_search')
]
