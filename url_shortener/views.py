from django.shortcuts import get_object_or_404, redirect
from ipware import get_client_ip
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from url_shortener.models import Shortener
from url_shortener.serializers import (
    UrlShortenerSerializer,
    UrlShortenerStatisticSerializer,
)


class UrlShortenerAPIView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UrlShortenerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_ip, _ = get_client_ip(request)

        shortener, _ = Shortener.objects.get_or_create(
            defaults={
                "created_by_user_agent": request.META.get("HTTP_USER_AGENT"),
                "created_by_ip": user_ip,
            },
            **serializer.data
        )

        response = {
            "short_url": request.build_absolute_uri(shortener.absolute_short_url),
        }
        return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request: Request, short_url: str) -> redirect:
        shortener = get_object_or_404(Shortener, short_url=short_url)

        shortener.views += 1
        shortener.save(update_fields=["views"])

        return redirect(shortener.long_url)


class UrlShortenerStatisticsAPIView(RetrieveModelMixin, GenericViewSet):
    serializer_class = UrlShortenerStatisticSerializer
    queryset = Shortener.objects.all()
    lookup_field = "short_url"
