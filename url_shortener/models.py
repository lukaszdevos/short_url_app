from django.conf import settings
from django.core.validators import URLValidator
from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string


def generate_short_url(num_char=settings.CHAR_LENGTH_IN_SHORT_URL) -> str:
    return get_random_string(num_char)


class Shortener(models.Model):
    long_url = models.TextField(unique=True, validators=[URLValidator()])
    short_url = models.CharField(
        max_length=10, unique=True, default=generate_short_url, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.created_at}"

    @property
    def absolute_short_url(self):
        return reverse("url_shortner:shortener_retrieve", args=[self.short_url])
