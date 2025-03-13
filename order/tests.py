from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import OrderCreateForm  # Import the correct form

class OrderFormTest(TestCase):
    
    def test_valid_form(self):
        form = OrderCreateForm(data={
            "name": "Divpreet",
            "email": "divpreet@gmail.com",
            "phone": "1234567890",
            "address": "Ludhiana, India",
            "division": "Dhaka",
            "district": "Dhaka",
            "zip_code": "141001",
            "payment_method": "Bkash",
            "account_no": "123456789012",
            "transaction_id": "987654"
        })
        self.assertTrue(form.is_valid())


    def test_invalid_form(self):
        form = OrderCreateForm(data={"name": "", "email": ""})
        self.assertFalse(form.is_valid())



        

