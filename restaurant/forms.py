from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Cook, Dish, DishType


# Form for creating and updating Dish instances
class DishForm(forms.ModelForm):
    # Allowing selection of multiple cooks for a dish using checkboxes
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = [
            "name",
            "description",
            "price",
            "dish_type",
            "cooks",
            "photo"
        ]


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


# Form for creating Cook instances, extending UserCreationForm to include authentication fields
class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "photo", "years_of_experience"
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["photo", "years_of_experience"]


# Form for searching dishes by type
class DishSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        label="",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by dish type"
            }
        )
    )


# Form for searching cooks by username
class CookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        label="",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )
