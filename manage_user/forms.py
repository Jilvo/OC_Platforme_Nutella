from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class ConnexionForm(AuthenticationForm):
    """ Form to log an User model, this form is passed to the login view"""

    class Meta:
        model = User
        fields = ["username", "password"]

    # username = forms.CharField(
    #     label= "username",
    #     max_length=30,
    #     required=True
    # )
    # password = forms.CharField(
    #     label="password",
    #     max_length=30,
    #     required=True
    # )


class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """

    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(user.password)  # set password properly before commit
        if commit:
            user.save()
        return user


# class UserRegisterForm(forms.Form):
#     """ Form to create user"""
#     pass
#     username = forms.CharField(
#         label= "username",
#         max_length=30,
#         required=True
#     )
#     password = forms.CharField(
#         label="password",
#         max_length=30,
#         widget=forms.PasswordInput,
#         required=True
#     )
#     email = forms.EmailField(
#         label="email",
#         max_length=30,
#         required=True
#     )
