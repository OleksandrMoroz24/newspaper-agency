from django.urls import path
from .views import (
    index,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    CookDetailView,
    CookListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishDetailView,
    DishListView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path('cook/add/', CookCreateView.as_view(), name='cook-add'),
    path('cook/<int:pk>/edit/', CookUpdateView.as_view(), name='cook-edit'),
    path('cook/<int:pk>/delete/', CookDeleteView.as_view(), name='cook-delete'),
    path('cook/<int:pk>/', CookDetailView.as_view(), name='cook-detail'),
    path('cook/', CookListView.as_view(template_name='restaurant/cook_list.html'), name='cook-list'),

    path('dish/add/', DishCreateView.as_view(), name='dish-add'),
    path('dish/<int:pk>/edit/', DishUpdateView.as_view(), name='dish-edit'),
    path('dish/<int:pk>/delete/', DishDeleteView.as_view(), name='dish-delete'),
    path('dish/<int:pk>/', DishDetailView.as_view(), name='dish-detail'),
    path('dish/', DishListView.as_view(template_name='restaurant/dish_list.html'), name='dish-list'),

    path('dish_types/', DishTypeListView.as_view(), name='dish_type_list'),
    path('dish_types/create/', DishTypeCreateView.as_view(), name='dish_type_add'),
    path('dish_types/update/<int:pk>/', DishTypeUpdateView.as_view(), name='dish_type_edit'),
    path('dish_types/delete/<int:pk>/', DishTypeDeleteView.as_view(), name='dish_type_delete'),
]

app_name = "restaurant"
