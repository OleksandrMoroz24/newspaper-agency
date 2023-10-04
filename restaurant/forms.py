from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Cook, Dish


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ['username', 'first_name', 'last_name', 'email', 'photo', 'years_of_experience']


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'dish_type', 'cooks', 'photo']


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", 'photo', 'years_of_experience'
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ['photo', 'years_of_experience']


class SearchForm(forms.Form):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Search...'}))