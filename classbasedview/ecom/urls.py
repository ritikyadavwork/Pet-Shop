from django.urls import path
from django.contrib.auth.decorators import login_required

from classbasedview.ecom.management import ProductAddView
from classbasedview.ecom.views import HomeView, SuperAdminDashboardView

app_name = "ecom"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
# super admin dashboard
urlpatterns += [
    path('dashbord/', login_required(SuperAdminDashboardView.as_view()), name="super_admin_dashboard"),
    path('add/product/', login_required(ProductAddView.as_view()), name="add_product"),
]
