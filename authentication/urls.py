from django.urls import path
from .views import RegisterView, LoginView
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Register New User
    path('login/', LoginView.as_view(), name='login'),  # Login User
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get JWT Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT Token
    
]
