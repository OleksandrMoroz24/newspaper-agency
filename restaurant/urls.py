from django.urls import path

from .views import (
    index,
    DishListView,
    DishDetailView,
)


urlpatterns = [
    path("", index, name="index"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    ]

app_name = "restaurant"
