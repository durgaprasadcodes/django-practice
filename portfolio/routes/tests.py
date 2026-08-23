from django.test import SimpleTestCase
from django.urls import reverse


class TemplateRenderingTests(SimpleTestCase):
    def test_home_page_renders_nav_and_footer(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Durga Prasad Kota")
        self.assertContains(response, "Footer age")

    def test_footer_page_renders(self):
        response = self.client.get(reverse("footer"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Footer age")
