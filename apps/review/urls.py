from django.urls import path
from .views import ReviewAPIView, ReviewDetailAPIView

urlpatterns = [
    path('reviews/', ReviewAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
]
