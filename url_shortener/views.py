from django.shortcuts import get_object_or_404, redirect
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from url_shortener.models import Shortener
from url_shortener.serializers import UrlShortenerSerializer


class UrlShortenerAPIView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UrlShortenerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        shortener, _ = Shortener.objects.get_or_create(**serializer.data)
        response = {
            "short_url": request.build_absolute_uri(shortener.absolute_short_url)
        }

        return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request: Request, short_url: str) -> redirect:
        shortener: Shortener = get_object_or_404(Shortener, short_url=short_url)

        return redirect(shortener.long_url)
