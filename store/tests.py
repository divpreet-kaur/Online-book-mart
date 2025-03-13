from django.test import TestCase, Client
from django.urls import reverse
from .models import Book, Category, Writer
from django.contrib.auth.models import User


class BookModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Fiction")
        self.writer = Writer.objects.create(name="Yugesh Verma", slug="yugesh-verma", bio="Author Bio")
        self.book = Book.objects.create(name="Django Guide", writer=self.writer, price=500, category=self.category, slug="django-guide", stock=10, description="A guide to Django.")

    def test_book_creation(self):
        self.assertEqual(self.book.name, "Django Guide")
        self.assertEqual(self.book.writer.name, "Yugesh Verma")
        self.assertEqual(self.book.price, 500)
        
class StoreViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_view(self):
        response = self.client.get(reverse('store:index')) # URL name from urls.py
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/index.html')


class UserAuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='divpreet', password='password123')

    def test_login(self):
        login = self.client.login(username='divpreet', password='password123')
        self.assertTrue(login)

