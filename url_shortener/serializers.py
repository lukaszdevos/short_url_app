from rest_framework import serializers

from url_shortener.models import Shortener


class UrlShortenerSerializer(serializers.Serializer):
    long_url = serializers.URLField()


class UrlShortenerStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = [
            "long_url",
            "absolute_short_url",
            "created_at",
            "views",
            "created_by_ip",
            "created_by_user_agent",
        ]
