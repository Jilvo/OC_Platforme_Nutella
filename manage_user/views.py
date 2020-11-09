from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import check_password
from .forms import ConnexionForm, RegistrationForm


def legal_mention(request):
    return render(request, "legal_mention.html")


# Create your views here.
def signin_function(request):
    return render(request, "login.html")


def signup_function(request):

    return render(request, "signup.html")


def register(request):
    if request.method == "GET":
        return render(request, "signup.html")
    # print(request.POST["password"])
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            try:
                user = form.save(commit=False)
                user.set_password(request.POST["password"])
                # user = User.objects.create_user(username,password,email)
                user.save()
                print(user.check_password(password))
                # print(user)
                login(request, user)  # nous connectons l'utilisateur
                messages.success(request, "Votre compte a bien été crée")
                print("Votre compte a bien été crée")
            except Exception as e:
                form = RegistrationForm()
                print(e)
                # messages.error("request, 'Votre compte n‘a pas été crée.'")
            return render(request, "index.html")
        else:
            return render(request, "index.html")


def connexion(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        print("déja connecté")
        return redirect("index.html")
    # if request.method == "GET":
    #     print("Voir la page sans se connecter")
    #     return render(request, 'login.html')
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        username = request.POST["username"]
        print(username)
        password = request.POST["password"]
        print(password)
        user = authenticate(
            username=username, password=password
        )  # Nous vérifions si les données sont correctes
        print(user)
        print(user.check_password(password))

        if user is not None:  # Si l'objet renvoyé n'est pas None
            login(request, user)  # nous connectons l'utilisateur
            # return redirect(user_page)
            print("Connecté")
            return redirect("index")
        else:  # sinon une erreur sera affichée

            print("Utilisateur inconnu ou mauvais de mot de passe.")
    else:
        # form = ConnexionForm()
        print("Rien ne se passe aucune connexion effectué")
    context = {"ConnexionForm": ConnexionForm()}
    return render(request, "login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("index")
