from django.urls import path
from .views import CardCategoriesListView, CardCategoriesCreateView, CardCategoriesUpdateView, CardCategoriesDeleteView


urlpatterns = [
    path('card_categories_list/', CardCategoriesListView.as_view(), name='card_categories_list'),
    path('card_categories_create/', CardCategoriesCreateView.as_view(), name='card_categories_create'),
    path('card_categories_update/<int:pk>/', CardCategoriesUpdateView.as_view(), name='card_categories_update'),
    path('card_categories_delete/<int:pk>/', CardCategoriesDeleteView.as_view(), name='card_categories_delete'),
]