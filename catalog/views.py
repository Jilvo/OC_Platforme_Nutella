from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from .models import Product, Category, UserFavorite


# Create your views here.
def home_function(request):
    # all_entries = Entry.objects.filter(name="Julien")
    # print(all_entries)
    return render(request, "index.html")


def searchresult(request):
    """search the product, if we find product with a name who
    contains the string of the query we disp 6 product
    if not we disp 10 product of the base"""
    query = request.GET.get("query", "")
    print(query)
    if not query:
        title = "Aucun champ rempli, affichage des 10 premiers produits"
        product = Product.objects.all()[0:10]
        context = {"product": product, "title": title}
    else:
        product = Product.objects.filter(name__contains=query)[:6]
        if not product:
            title = (
                "Votre recherche, "
                + query
                + ", n'a donné aucun résultat,"
                + "affichage des 10 premiers produits"
            )
            product = Product.objects.all()[0:10]
            context = {"title": title, "product": product}
        else:
            title = str("Votre recherche est :" + " " + query)
            context = {"title": title, "product": product}
    print(product)
    return render(request, "search_result.html", context)


def choosen_product(request):
    """ display the detail page for the product """
    query = request.GET.get("product_name", "")
    print(query)
    product = Product.objects.get(name=query)
    print(product)
    lst_cat = []
    # cat = Product.category.all()
    for cat in product.category.all():
        print(cat)
        lst_cat.append(cat)
    # cat = Category.objects.get(name=product.cat)
    sub_product = Product.objects.filter(category=lst_cat[0]).order_by(
        "nutrition_grade"
    )[:6]
    print(type(sub_product))
    context = {"product": product, "sub_product": sub_product}
    print(sub_product)
    return render(request, "choosen_product.html", context)


@login_required
def add_favorite(request):
    """Add the product selected in the list of favorite of the user"""
    print("La fonction pour ajouté un produit est appelé")
    query = request.GET.get("_substitute_product", "")
    print(query)
    # query_favorite = query.id
    query_name = Product.objects.get(name=query)
    print(query_name)
    print("ID DU PRODUIT")
    username = request.user
    # user_id = request.user.id
    # # user = User.objects.get(id=username)
    print(username)
    print("ID DE L'USER")
    if query_name is not None:
        try:
            UserFavorite.objects.get(user_name=username, product=query_name)
            print("Ce produit est déjà dans vos favoris.")
            return redirect("see_favorits")
        except ObjectDoesNotExist:
            new_favorite = UserFavorite.objects.create(
                user_name=username, product=query_name
            )
            new_favorite.save()
            print("Le produit a bien été enregistré.")
            return redirect("see_favorits")
    else:
        pass
    return redirect("see_favorits ")
    # return render(request,'index.html')


@login_required
def see_favorits(request):
    """See the favorits of the User"""
    user_name = request.user
    print(user_name)
    # product = UserFavorite.objects.filter(user_name=user_name)
    list_favorits = UserFavorite.objects.all().filter(user_name=user_name)
    favorits_query = list_favorits
    favorits_list = []
    for favorite in favorits_query:
        favorits_list.append(Product.objects.get(pk=favorite.product.id))
    print(favorits_list)
    context = {
        # 'product' : product,
        "user_name": user_name,
        "product": favorits_list,
    }

    return render(request, "favorits.html", context)


@login_required
def remove_favorits(request):
    pass
#     return render(request, "index.html")
#     # """remove one product from the favorits"""
#     # product = request.GET.get("delete_prod", "")
#     # print("Nom du produit")
#     # print(product)
#     # user_name = request.user
#     # print('nom de luser')
#     # print(user_name)
#     # if product is not None:
#     #     del_prod = UserFavorite.objects.filter(
#     #          user_name=user_name,
#     #          product=product)
 
#     #     # Category.objects.filter().delete(del_prod)
#     #     # print(del_prod.id)
#     # else:
#     #     pass
#     # context = {"product": product}
#     # return render(request, "favorits.html", context)
