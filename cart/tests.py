from django.test import TestCase, Client
from django.urls import reverse
from store.models import Book, Category, Writer  # Ensure Writer is imported
from django.contrib.auth.models import User

class CartTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create a Category
        self.category = Category.objects.create(
            name="Fiction",
            slug="fiction"
        )

        # Create a Writer (since Book requires it)
        self.writer = Writer.objects.create(
            name="John Doe",
            slug="john-doe",
            bio="Test writer bio"
        )

        # Create a Book with required fields
        self.book = Book.objects.create(
            writer=self.writer,  # Assign writer here
            category=self.category,
            name="Test Book",
            slug="test-book",
            price=100,
            stock=10,
            coverpage="cover.jpg",
            bookpage="book.pdf",
            description="Test Description"
        )

    def test_add_to_cart(self):
        response = self.client.post(reverse('cart:cart_add', args=[self.book.id]), {'quantity': 2})
        self.assertEqual(response.status_code, 302)

