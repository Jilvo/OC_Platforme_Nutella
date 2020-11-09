from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from catalog.models import UserFavorite, Product, Category

# Create your tests here.


class DetailPageTestCase(TestCase):
    """Test detail pages"""

    # ran before each test.
    def setUp(self):
        """setUp"""
        self.product = Product()
        self.category = Category.objects.create(name="Saumons, Poissons")
        self.user = User.objects.get(username="test_user")
        self.product = Product.objects.create(
            name="SOMETHING_WITH_NUTRI_SCORE_A",
            category=self.category,
            description="nothing",
            nutriscore="A",
            stores="LECLERC",
            image="img/...",
            brand="Django",
            calories="49",
            lipids="78",
            sugars="8",
            proteins="7",
            salts="8",
            url_off="https://...",
            id="74",
        )
        self.product.save()

    # def test_detail_page_returns_200(self):
    #     """test that detail page returns a 200 if the item exists"""
    #     product_id = self.product.id
    #     response = self.client.get(reverse('index', args=(product_id)))
    #     self.assertEqual(response.status_code, 200)


class Favorites(TestCase):
    """Class Favorits"""

    def create_fav(self):
        DetailPageTestCase.setUp(self)
        self.my_user = User.objects.create(id=5, username="Testuser")
        self.favorite = None


class PageTestCase(TestCase):
    """class PageTestCase"""

    def setUp(self):
        """setUp"""
        self.product = Product()
        self.category = Category.objects.create(name="Saumons, Poissons")
        self.user = User.objects.get(username="test_user")
        self.product = Product.objects.create(
            name="SOMETHING_WITH_NUTRI_SCORE_A",
            category=self.category,
            description="nothing",
            nutriscore="A",
            stores="LECLERC",
            image="img/...",
            brand="Django",
            calories="49",
            lipids="78",
            sugars="8",
            proteins="7",
            salts="8",
            url_off="https://...",
        )
        self.product.save()

    def test_choosen_product_page(self):
        """test_choosen_product_page"""
        response = self.client.get(
            reverse("choosen_product"),
            {
                "product_name": "SOMETHING_WITH_NUTRI_SCORE_A",
            },
        )
        self.assertEqual(response.status_code, 200)

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
