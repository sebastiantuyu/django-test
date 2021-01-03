"""  Creacion de FORMS usando el model FORM """

from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        """
        Clase que modifica los campos del Form
        """
        model = Post
        fields = ('user','profile','title','photo')