from rest_framework import serializers


class UrlShortenerSerializer(serializers.Serializer):
    long_url = serializers.URLField()
