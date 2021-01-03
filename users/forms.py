""" Aqui van los forms """

from django import forms

class ProfileForm(forms.Form):

    website = forms.URLField(max_length=200, required=True)
    bio = forms.CharField(max_length=500,required=False)
    picture = forms.ImageField()
    phone_number = forms.CharField(max_length=20,required=False)
