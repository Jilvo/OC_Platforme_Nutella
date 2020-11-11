"""oc_8_projet_nutella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from catalog import views as catalog_views
from manage_user import views as manage_user_views


urlpatterns = [
    path("administration/", admin.site.urls),
    path("404", manage_user_views.page_not_found_view),
    path("500", manage_user_views.page_internal_error),
    path("legal_mention", manage_user_views.legal_mention, name="legal_mention"),
    path("", catalog_views.home_function, name="index"),
    path("login", manage_user_views.connexion, name="login"),
    path("logout", manage_user_views.logout_view, name="logout"),
    path("signup", manage_user_views.register, name="signup"),
    # path('search_result',catalog_views.searchresult),
    path("search_result", catalog_views.searchresult, name="search_result"),
    path("choosen_product", catalog_views.choosen_product, name="choosen_product"),
    path("addfavorits", catalog_views.add_favorite, name="add_favorits"),
    path("favorits", catalog_views.see_favorits, name="see_favorits"),
    path("delete_fav", catalog_views.remove_favorits, name="delete_fav"),
]
