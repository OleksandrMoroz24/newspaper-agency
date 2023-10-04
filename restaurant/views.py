from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from restaurant.models import Dish, DishType, Cook
from restaurant.forms import (
    DishForm,
    DishTypeForm,
    CookCreationForm,
    CookUpdateForm,
    DishSearchForm,
    CookSearchForm
)


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
    form_class = CookSearchForm
    paginate_by = 7

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            return Cook.objects.filter(username__icontains=query)
        else:
            return Cook.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form_class(self.request.GET)
        return context


class DishListView(ListView, LoginRequiredMixin):
    model = Dish
    template_name = 'restaurant/dish_list.html'
    form_class = DishSearchForm
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            return Dish.objects.filter(dish_type__name__icontains=query
                                       ).select_related("dish_type")
        else:
            return Dish.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form_class(self.request.GET)
        return context


class DishTypeListView(ListView):
    model = DishType
    template_name = 'restaurant/dish_type_list.html'
    paginate_by = 10


class DishTypeCreateView(CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = 'restaurant/dish_type_form.html'
    success_url = reverse_lazy("restaurant:dish_type_list")


class DishTypeUpdateView(UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = 'restaurant/dish_type_form.html'
    success_url = reverse_lazy("restaurant:dish_type_list")


class DishTypeDeleteView(DeleteView):
    model = DishType
    template_name = 'restaurant/dish_type_confirm_delete.html'
    success_url = reverse_lazy("restaurant:dish_type_list")
