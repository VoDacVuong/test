from . import views
from django.urls import path

urlpatterns = [
    path("", views.IndexClass.as_view())
]
