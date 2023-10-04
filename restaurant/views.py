
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from restaurant.models import Dish, DishType, Cook
from restaurant.forms import CookForm, DishForm, SearchForm, CookCreationForm, CookUpdateForm


@login_required
def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1,
    }

    return render(request, "restaurant/index.html", context=context)


class CookCreateView(CreateView, LoginRequiredMixin):
    model = Cook
    form_class = CookCreationForm
    template_name = 'restaurant/cook_form.html'
    success_url = reverse_lazy("restaurant:cook-list")


class CookUpdateView(UpdateView, LoginRequiredMixin):
    model = Cook
    form_class = CookUpdateForm
    template_name = 'restaurant/cook_form.html'
    success_url = reverse_lazy("restaurant:cook-list")


class CookDeleteView(DeleteView, LoginRequiredMixin):
    model = Cook
    success_url = reverse_lazy("restaurant:cook-list")
    template_name = 'restaurant/cook_confirm_delete.html'


class CookDetailView(DetailView, LoginRequiredMixin):
    model = Cook
    template_name = 'restaurant/cook_detail.html'


class DishCreateView(CreateView, LoginRequiredMixin):
    model = Dish
    form_class = DishForm
    template_name = 'restaurant/dish_form.html'
    success_url = reverse_lazy("restaurant:dish-list")


class DishUpdateView(UpdateView, LoginRequiredMixin):
    model = Dish
    form_class = DishForm
    template_name = 'restaurant/dish_form.html'
    success_url = reverse_lazy("restaurant:dish-list")


class DishDeleteView(DeleteView, LoginRequiredMixin):
    model = Dish
    success_url = reverse_lazy("restaurant:dish-list")
    template_name = 'restaurant/dish_confirm_delete.html'


class DishDetailView(DetailView, LoginRequiredMixin):
    model = Dish
    template_name = 'restaurant/dish_detail.html'


class CookListView(ListView, LoginRequiredMixin):
    model = Cook
    template_name = 'restaurant/cook_list.html'
    form_class = SearchForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            return Cook.objects.filter(username__icontains=query)
        return Cook.objects.all()


class DishListView(ListView, LoginRequiredMixin):
    model = Dish
    template_name = 'restaurant/dish_list.html'
    form_class = SearchForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            return Dish.objects.filter(name__icontains=query)
        return Dish.objects.all()
