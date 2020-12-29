""" Dar acceso a todas la funcion para registrar el modelo Profile en el ADMIN de Django"""

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from users.models import Profile
# Register your models here.
#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Detalles al la lista de Profiles mostrados en la consola del ADMIN """
    list_display = ('pk','user','phone_number','website','picture')
    list_display_links = ('pk','user',)
    list_editable = ('phone_number',)
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
    )

    fieldsets = (
        ('Profile',{
            'fields': (
                ('user','picture'),
                ('phone_number','website'),
                ('bio'),
            ),
        }),
        ('Metadata',{'fields':('last','created',)})
    )

    readonly_fields = ('created','last',)


class ProfileInline(admin.StackedInline):
        """ Agrega los campos del modelo Profile en los campos
        de user cuando se edita en la consola del ADMIN """

        model = Profile
        can_delete = False
        verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
         """ Agregar profile admin a la base del administrador de usuario """
         inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)