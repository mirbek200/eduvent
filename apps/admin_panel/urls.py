from django.urls import path
from .views import (CardCategoriesListView, CardCategoriesCreateView, CardCategoriesUpdateView, CardCategoriesDeleteView,
                    SubcategoriesListView, SubcategoriesCreateView, SubcategoriesUpdateView, SubcategoriesDeleteView)


urlpatterns = [
    path('card_categories_list/', CardCategoriesListView.as_view(), name='card_categories_list'),
    path('card_categories_create/', CardCategoriesCreateView.as_view(), name='card_categories_create'),
    path('card_categories_update/<int:pk>/', CardCategoriesUpdateView.as_view(), name='card_categories_update'),
    path('card_categories_delete/<int:pk>/', CardCategoriesDeleteView.as_view(), name='card_categories_delete'),

    path('sub_categories_list/', SubcategoriesListView.as_view(), name='sub_categories_list'),
    path('sub_categories_create/', SubcategoriesCreateView.as_view(), name='sub_categories_create'),
    path('sub_categories_update/<int:pk>/', SubcategoriesUpdateView.as_view(), name='sub_categories_update'),
    path('sub_categories_delete/<int:pk>/', SubcategoriesDeleteView.as_view(), name='sub_categories_delete'),
]
