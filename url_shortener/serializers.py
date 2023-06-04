from ipware import get_client_ip
from rest_framework import serializers

from url_shortener.models import Shortener


class UrlShortenerSerializer(serializers.ModelSerializer):
    long_url = serializers.CharField(max_length=255, validators=[])
    
    class Meta:
        model = Shortener
        fields = [
            "long_url",
        ]
        
    def to_representation(self, instance: Shortener) -> dict[str, str]:
        return {"short_url": self.context["request"].build_absolute_uri(instance.absolute_short_url)}

    def create(self, validated_data: dict[str, str]) -> Shortener:
        request = self.context["request"]
        user_ip, _ = get_client_ip(request)
        
        shortener, _ = Shortener.objects.get_or_create(
            defaults={
                "created_by_user_agent": request.META.get("HTTP_USER_AGENT"),
                "created_by_ip": user_ip,
            },
            **validated_data
        )
        
        return shortener
    

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
