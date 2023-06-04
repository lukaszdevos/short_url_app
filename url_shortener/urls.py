from django.urls import path

from url_shortener.views import UrlShortenerAPIView, UrlShortenerStatisticsAPIView

app_name = "url_shortner"


urlpatterns = [
    path("", UrlShortenerAPIView.as_view({"post": "create"}), name="shortener_create"),
    path("<str:short_url>/", UrlShortenerAPIView.as_view({"get": "retrieve"}), name="shortener_retrieve"),
    path(
        "statistics/<str:short_url>/",
        UrlShortenerStatisticsAPIView.as_view({"get": "retrieve"}),
        name="shortener_statistic_retrieve",
    ),
]
