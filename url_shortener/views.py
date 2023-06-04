from django.shortcuts import redirect
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet

from url_shortener.models import Shortener
from url_shortener.serializers import (
    UrlShortenerSerializer,
    UrlShortenerStatisticSerializer,
)


class UrlShortenerAPIView(RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Shortener.objects.all()
    serializer_class = UrlShortenerSerializer
    lookup_field = "short_url"

    def retrieve(self, request: Request, *args, **kwargs) -> redirect:
        instance = self.get_object()
        instance.views += 1
        instance.save(update_fields=["views"])

        return redirect(instance.long_url)


class UrlShortenerStatisticsAPIView(RetrieveModelMixin, GenericViewSet):
    serializer_class = UrlShortenerStatisticSerializer
    queryset = Shortener.objects.all()
    lookup_field = "short_url"
