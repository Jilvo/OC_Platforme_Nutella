from django.test import TestCase
from django.urls import reverse,NoReverseMatch
from django.contrib.auth.models import User
from oc_8_projet_nutella.wsgi import get_wsgi_application, application, os
from catalog.models import UserFavorite, Product, Category
from catalog.selenium_tests import Selenium_test
# # Create your tests here.

class DetailPageTestCase(TestCase):
    """class DetailPageTestCase"""
    def setUp(self):
        """Create somme products, user and favorites in the database"""
        self.steak = Product.objects.create(name='Steak', nutrition_grade='e',  url="https://test.com",
            calories='49',
            lipids='78',
            sugars='8',
            proteins='7',
            salts='8',
            id='74')
        self.poulet = Product.objects.create(name='Poulet', nutrition_grade='d',  url="https://test.com")
        self.product_id = Product.objects.get(name='Steak')
        self.substitute_id = Product.objects.get(name='Poulet')
        user_with_favorite = User.objects.create(username='test_user')
        user_without_favorite = User.objects.create(username='no_favorite_user')
        self.user = User.objects.get(username='test_user')
        self.no_favorite_user = User.objects.get(username='no_favorite_user')
        favorite = UserFavorite.objects.create(user_name=self.user, product=self.substitute_id)

    def test_search_contain_return_context(self):
        """Test that "stea" query return the "steak" product """
        user_search_stea = "stea"
        user_search_void = ""
        response = self.client.get(reverse("search_result"), context={'query': user_search_stea})
        product_returned = response.context['product'][0].name
        response_void = self.client.get(reverse("search_result"), context={'query': user_search_void})
        product_returned_void = response_void.context['title']
        self.assertEqual(product_returned, 'Steak')
        self.assertEqual(product_returned_void, 'Aucun champ rempli, affichage des 10 premiers produits')
    
    # def test_add_fav(self):

    def test_favorites_return_context(self):
        """Test that 'favorites' view 'Poulet' if the user is logged-in"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('see_favorits'))
        favorite_returned = response.context['product'][0].name
        self.assertEqual(favorite_returned, 'Poulet')

    def test_not_existing_substitute_page(self):
        """test no substitute page"""
        try:
            response = self.client.get(reverse('choosen_product'), {
                'query': 'NOTHING',
            })
            self.assertEqual(response.status_code, 404)
        except:
            pass

    def test_simple_product(self):
        """test simple product """
        test_steak = Product.objects.filter(name='Steak')
        t_t = test_steak[0]
        self.assertEqual('78', t_t.lipids)
        self.assertEqual(74, t_t.id)
        self.assertNotEqual('2318', t_t.proteins)

class NoReverse(TestCase):
    """Class NoReverse"""
    def test_fake_page(self):
        """test fake page"""
        try:
            response = self.client.get(reverse('fake'))
            self.assertRaisesMessage(NoReverseMatch, response)
        except NoReverseMatch:
            pass

class PageTestCase(TestCase):
    """class PageTestCase"""

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

    def test_index_page(self):
        """test_index_page"""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_legal_mention(self):
        """test_legal_mention"""
        response = self.client.get(reverse("legal_mention"))
        self.assertEqual(response.status_code, 200)

    def test_search_result_page(self):
        """test_search_result_page"""
        response = self.client.get(reverse("search_result"))
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

class OsTest(TestCase):
    """Class os"""
    def test_wsgi(self):
        """test wsgi"""
        self.assertEqual(type(application), type(get_wsgi_application()))