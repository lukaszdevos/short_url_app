from factory import DictFactory, Sequence
from factory.django import DjangoModelFactory

from url_shortener.models import Shortener


class UrlFactory(DictFactory):
    long_url = Sequence(lambda n: f"https://example.com/{n + 1}")


class ShortenerFactory(DjangoModelFactory):
    class Meta:
        model = Shortener

    long_url = Sequence(lambda n: f"https://example.com/long/url/{n + 1}")
