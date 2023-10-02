from django import forms
from .models import Cook, Dish


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ['username', 'first_name', 'last_name', 'email', 'photo', 'years_of_experience']


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'dish_type', 'cooks', 'photo']


class SearchForm(forms.Form):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Search...'}))