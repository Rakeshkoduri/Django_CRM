from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class Register(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'first_name', "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'last_name', "class": "form-control"}), label="")
    email = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(attrs={'placeholder': 'email', "class": "form-control"}),
                            label="")
    address = forms.CharField(required=True,
                              widget=forms.widgets.TextInput(attrs={'placeholder': 'address', "class": "form-control"}),
                              label="")
    city = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(attrs={'placeholder': 'city', "class": "form-control"}),
                           label="")
    state = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(attrs={'placeholder': 'state', "class": "form-control"}),
                            label="")
    pincode = forms.CharField(required=True,
                              widget=forms.widgets.TextInput(attrs={'placeholder': 'pincode', "class": "form-control"}),
                              label="")


    class Meta:
        model = Record
        exclude = ("user",)
