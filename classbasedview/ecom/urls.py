from django.urls import path
from django.contrib.auth.decorators import login_required
from classbasedview.ecom.views import HomeView

app_name = "ecom"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
