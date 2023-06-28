from django.urls import path
from .views import (
    CardCreateView,
    CardListView,
    CardUpdateView,
    CardDeleteView
)


urlpatterns = [
    path('card_list/', CardListView.as_view(), name='card_list'),
    path('card_create/', CardCreateView.as_view(), name='card_create'),
    path('card_update/<int:pk>/', CardUpdateView.as_view(), name='card_update'),
    path('card_delete/<int:pk>/', CardDeleteView.as_view(), name='card_delete'),
]
