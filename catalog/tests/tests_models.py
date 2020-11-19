from django.test import TestCase
from django.contrib.auth.models import User
from catalog.models import UserFavorite,Product,Category

# Create your tests here.

class ProductModelTest(TestCase):
    def test_productmodel(self):
        product = Product(name='8 steaks hachés façon bouchère')
        self.assertEqual(str(product), product.name)

class UserFavoriteModelTest(TestCase):
    def test_userfavoritemodel(self):
        product = Product(name='8 steaks hachés façon bouchère')
        user = 'test1'
        product_name = UserFavorite(user_name=User(username=user),product=product)
        self.assertEqual(str(product), str(product))

class CategoryModelTest(TestCase):
    def test_categorymodel(self):
        product = Category(name='Viande')
        self.assertEqual(str(product), product.name)
