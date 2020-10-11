from django.urls import path
from .views import Index, Login, Logout

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout, name="logout")
]