from rest_framework.routers import SimpleRouter
from rest_framework.urls import path

from .viewsets import ShortenerViewSet

router = SimpleRouter(trailing_slash=False)

urlpatterns = [
    path("shortener", ShortenerViewSet.as_view({"post": "create"}), name="create-shorteners"),
    path("<str:short_url>", ShortenerViewSet.as_view({"get": "redirect"}), name="redirect-shorteners"),
    path("<str:short_url>/+", ShortenerViewSet.as_view({"get": "statistics"}), name="statistics-shorteners"),
]
