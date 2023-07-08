from django.urls import path
from .views import ReviewListAPIView, ReviewDetailAPIView

urlpatterns = [
    path('review/', ReviewListAPIView.as_view(), name='reviews_list'),
    path('review_detail/<int:id>/', ReviewDetailAPIView.as_view(), name='review_detail'),
]
