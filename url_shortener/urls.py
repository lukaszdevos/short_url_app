from django.urls import path

from url_shortener.views import UrlShortenerAPIView

app_name = "url_shortner"


urlpatterns = [
    path("", UrlShortenerAPIView.as_view(), name="shortener_create"),
    path("<str:short_url>/", UrlShortenerAPIView.as_view(), name="shortener_retrieve"),
]