from django.urls import path
from .views import IndexView, LoginView, Logout

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', Logout, name="logout")
]
