from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from catalog.models import UserFavorite, Product, Category

# # Create your tests here.
class DetailPageTestCase(TestCase):
    """class DetailPageTestCase"""
    def setUp(self):
        """Create somme products, user and favorites in the database"""
        steak = Product.objects.create(name='Steak', nutrition_grade='e',  url="https://test.com")
        poulet = Product.objects.create(name='Poulet', nutrition_grade='d',  url="https://test.com")
        self.product_id = Product.objects.get(name='Steak')
        self.substitute_id = Product.objects.get(name='Poulet')
        user_with_favorite = User.objects.create(username='test_user')
        user_without_favorite = User.objects.create(username='no_favorite_user')
        self.user = User.objects.get(username='test_user')
        self.no_favorite_user = User.objects.get(username='no_favorite_user')
        favorite = UserFavorite.objects.create(user_name=self.user, product=self.substitute_id)

    def test_search_return_context(self):
        """Test that "stea" query return the "steak" product """
        user_search = "stea"
        response = self.client.post(reverse("search_result"), context={'query': user_search,})
        product_returned = response.context['product'][0].name
        self.assertEqual(product_returned, 'Steak')

    def test_favorites_return_context(self):
        """Test that 'favorites' view 'Poulet' if the user is logged-in"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('see_favorits'))
        favorite_returned = response.context['product'][0].name
        self.assertEqual(favorite_returned, 'Poulet')


# class Favorites(TestCase):
#     """Class Favorits"""

#     def create_fav(self):
#         DetailPageTestCase.setUp(self)
#         self.my_user = User.objects.create(id=5, username="Testuser")
#         self.favorite = None


class PageTestCase(TestCase):
    """class PageTestCase"""
    def test_favorits_page(self):
        """test_favorits_page"""
        response = self.client.get(reverse("see_favorits"))
        self.assertEqual(response.status_code, 302)

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
