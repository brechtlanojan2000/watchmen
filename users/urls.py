from django.urls import path
from .views import UserRegisterView, UserDashboardView, UserUpdateView

urlpatterns = [
    path('', UserDashboardView.as_view(), name='user-dashboard'),
    path('register', UserRegisterView.as_view(), name='user-register'),
    path('<int:user_id>', UserUpdateView.as_view(), name='user-update')
]