""" Aqui van los forms """

from django import forms
from .models import User,Profile

class ProfileForm(forms.Form):

    website = forms.URLField(max_length=200, required=True)
    bio = forms.CharField(max_length=500,required=False)
    picture = forms.ImageField()
    phone_number = forms.CharField(max_length=20,required=False)


class SignupForm(forms.Form):

    username = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
    password = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'})
    )
    password_confirmation = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation','class':'form-control'})
    )

    email = forms.CharField(min_length=6,max_length=70, widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))
    first_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder':'First name','class':'form-control'}))
    last_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder':'Last name','class':'form-control'}))


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
        return data

    def save(self):
        """ Save the form, and create a User and a Profile """
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()