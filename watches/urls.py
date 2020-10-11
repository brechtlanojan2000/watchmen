from django.urls import path
from .views import WatchRegisterView, WatchDashboardView, WatchUpdateView, BrandRegisterView, BrandDashboardView

urlpatterns = [
    path('', WatchDashboardView.as_view(), name="watch-dashboard"),
    path('register', WatchRegisterView.as_view(), name="watch-register"),
    path('<int:watch_id>', WatchUpdateView.as_view(), name="watch-update"),
    path('brands', BrandDashboardView.as_view(), name="brand-dashboard"),
    path('brands/register', BrandRegisterView.as_view(), name="brand-register"),
]