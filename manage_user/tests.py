from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from catalog.models import UserFavorite,Product
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

    def test_register(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        logged_in = self.client.login(username='testuser', password='12345')
        self.assertTrue(logged_in)
        response = self.client.get("/")
        self.assertEqual(response.status_code , 200)


    

