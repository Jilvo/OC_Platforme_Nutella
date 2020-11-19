from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from catalog.models import UserFavorite,Product
from catalog.tests import DetailPageTestCase
# Create your tests here.

class PageTestCase(TestCase):
    """class PageTestCase"""
    def test_legal_mention(self):
        """test_legal_mention"""
        response = self.client.get(reverse('legal_mention'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """test_login_page"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        """test_signup_page"""
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_404_page(self):
        """test_404_page"""
        response = self.client.get(reverse('404'))
        self.assertEqual(response.status_code, 200)

    def test_500_page(self):
        """test_500_page"""
        response = self.client.get(reverse('500'))
        self.assertEqual(response.status_code, 200)

class StatusTestCase(TestCase):
    """ class StatusTestCase """
    def test_login(self):
        """test_login """
        response = self.client.post(reverse('index'),
                                    {'username': 'testuser', 'password': 'password'}, follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_user(self):
        """test fake user"""
        response = self.client.login(username="fake", password="fake")
        self.assertFalse(response)