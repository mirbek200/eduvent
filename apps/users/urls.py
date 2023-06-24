from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginView, RegistrationAPIView, ActivationView, ProfileUpdateAPIView, ProfileDetailAPIView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('activation/<str:activation_code>/', ActivationView.as_view()),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),

    path('profile_update/<int:pk>/', ProfileUpdateAPIView.as_view(), name='profile_update'),
    path('profile_detail/<int:pk>/', ProfileDetailAPIView.as_view(), name='profile_detail'),

]
