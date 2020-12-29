from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):

    """
    Extension de usuario mediante el modelo Proxy

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200,blank=True)
    bio = models.TextField(null=True)
    phone_number = models.CharField(max_length=10,blank=True)

    picture = models.ImageField(
        upload_to='users/pictures',
        null=True,
        blank=True,
          )

    created = models.DateTimeField(auto_now_add=True)
    last = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Regresar el nombre de usuario formateado """
        return self.user.username