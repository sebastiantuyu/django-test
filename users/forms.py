""" Aqui van los forms """

from django import forms
from .models import User

class ProfileForm(forms.Form):

    website = forms.URLField(max_length=200, required=True)
    bio = forms.CharField(max_length=500,required=False)
    picture = forms.ImageField()
    phone_number = forms.CharField(max_length=20,required=False)


class SignupForm(forms.Form):

    username = forms.CharField(max_length=70)
    password = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput()
    )

    email = forms.CharField(min_length=6,max_length=70)
    first_name = forms.CharField(max_length=15)
    last_Name = forms.CharField(max_length=15)


    def clean_username(self):
        """ Solo debe existir un unico usuario con el username """

        username = self.cleaned_data['username']
        user_taken = User.objects.filter(username=username).exists()
        if user_taken:
            raise forms.ValidationError('El usuario ya existe.')
        return username

    def clean(self):
        """  Confirmacion del password debe ser igual """
        # Super clean llama a la clase antes de ser modificada, si es que se modifica
        data = super().clean()
        password = data['password']
        password_conf = data['password_confirmation']
        if password != password_conf:
            raise forms.ValidationError('La contraseñas deben ser iguales.')
        return password

