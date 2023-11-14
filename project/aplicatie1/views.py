from django.urls import reverse
from django.views.generic import ListView, CreateView

from aplicatie1.models import Location


class LocationView(ListView):

    model = Location
    template_name = 'aplicatie1/location_index.html'


class CreateLocationView(CreateView):

    model = Location
    fields = ['city', 'country']
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('aplicatie1:lista_locatii')
