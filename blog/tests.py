from django.test import TestCase, Client
from django.urls import reverse
from .models import Blog
# Create your tests here.
class ExampleViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_GET(self):
        response = self.client.get(reverse('blog:all_blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/all_blogs.html')  # Ispravljeno ime šablona

    def test_detail_GET(self):
        # Pravite test za detail view
        response = self.client.get(reverse('blog:detail', args=[1]))  # Zamoljen je primer sa argumentom 1, prilagodite ga svojim potrebama
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/detail.html')  # Ispravljeno ime šablona

