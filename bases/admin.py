from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import Usuario


class UsuarioAdmin(UserAdmin):
    pass

admin.site.register(Usuario)
