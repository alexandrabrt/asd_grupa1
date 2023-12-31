from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie1.models import Location


class LocationView(LoginRequiredMixin, ListView):

    model = Location
    template_name = 'aplicatie1/location_index.html'
    paginate_by = 5


class CreateLocationView(LoginRequiredMixin, CreateView):

    model = Location
    fields = ['city', 'country']
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('aplicatie1:lista_locatii')


class UpdateLocationView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'forms.html'

    def test_func(self):
        user_location = self.request.user.userextend.location.id
        if ((get_location := Location.objects.filter(id=self.kwargs['pk'])) and
                get_location.exists() and
                user_location == get_location.first().id):
            return True
        return False

    def get_success_url(self):
        return reverse('aplicatie1:lista_locatii')


@login_required
def deactivate_location(request, pk):
    Location.objects.filter(id=pk).update(active=False)
    return redirect('aplicatie1:lista_locatii')


@login_required
def activate_location(request, pk):
    Location.objects.filter(id=pk).update(active=True)
    return redirect('aplicatie1:lista_locatii')
