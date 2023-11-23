from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Select

from userprofile.models import UserExtend


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'username', 'location']

        widgets = {
            "first_name": TextInput(attrs={"placeholder": "First name", "class": "form-control"}),
            "last_name": TextInput(attrs={"placeholder": "Last name", "class": "form-control"}),
            "email": TextInput(attrs={"placeholder": "Email", "class": "form-control"}),
            "username": TextInput(attrs={"placeholder": "Username", "class": "form-control"}),
            "location": Select(attrs={"placeholder": "Location", "class": "form-control"}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        field_data = self.cleaned_data
        username_value = field_data.get('username')
        if self.pk:
            if User.objects.filter(username=username_value).exclude(id=self.pk).exists():
                self._errors['username'] = self.error_class(["Usernameul deja exista! "
                                                             "Te rugam sa alegi alte valori"])
        else:
            if User.objects.filter(username=username_value).exists():
                self._errors['username'] = self.error_class(["Usernameul deja exista! "
                                                          "Te rugam sa alegi alte valori"])
        return field_data
