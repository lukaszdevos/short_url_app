from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from url_shortener.tests.url_shortener_factories import ShortenerFactory, UrlFactory


class TestUrlShortener(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url_create = reverse("url_shortner:shortener_create")

    def test_short_url_create(self):
        payload = UrlFactory.build()

        response = self.client.post(self.url_create, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.json().get("short_url"))

    def test_get_existing_short_url_when_long_url_exists(self):
        data = {"long_url": "https://newexample.com"}
        shortener = ShortenerFactory.create(**data)
        payload = UrlFactory.build(**data)

        response = self.client.post(self.url_create, payload)

        self.assertIn(shortener.short_url, response.json().get("short_url"))

    def test_redirection_to_long_url(self):
        shortener = ShortenerFactory.create()

        url_get = reverse("url_shortner:shortener_retrieve", args=[shortener.short_url])
        self.client.get(url_get)

        self.assertTrue(status.is_redirect(status.HTTP_302_FOUND))

    def test_redirection_to_long_url_when_does_not_exists(self):
        url_get = reverse("url_shortner:shortener_retrieve", args=["not_exists"])

        response = self.client.get(url_get)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
