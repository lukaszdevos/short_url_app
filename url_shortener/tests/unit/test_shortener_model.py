from django.conf import settings
from django.test import TestCase

from url_shortener.tests.url_shortener_factories import ShortenerFactory


class TestShortener(TestCase):
    def setUp(self) -> None:
        self.shortener = ShortenerFactory.build()

    def test_shortener_instance(self):
        self.assertEqual(
            str(self.shortener), f"{self.shortener.id} - {self.shortener.created_at}"
        )

    def test_default_short_url(self):
        self.assertEqual(
            len(self.shortener.short_url), settings.CHAR_LENGTH_IN_SHORT_URL
        )

    def test_absolute_short_url(self):
        self.assertEqual(self.shortener.absolute_short_url, f"/shortener/{self.shortener.short_url}/")
