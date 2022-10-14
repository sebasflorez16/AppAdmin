from tabnanny import verbose
from django.db import models
#from django.utils.http import urlquote
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UsuarioManager
from simple_history.models import HistoricalRecords
# Create your models here.


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electronico', unique=True)
    first_name = models.CharField('Nombre', max_length=80, blank=True)
    last_name = models.CharField('Apellidos', max_length=80, blank=True)
    is_staff = models.BooleanField(_('Es Staaff'), default=False,
        help_text=_('Indica si el usuario puede iniciar sesion en el admin'))
    is_active = models.BooleanField(_('Activo'), default=False,
        help_text=_('Designa si el usuario esta o no activo'))
    historical = HistoricalRecords()
    


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =['email','first_name','last_name']

    #Sobre escribir el objects del modelo
    objects = UsuarioManager()



    class Meta:
        verbose_name =_('Usuario')
        verbose_name_plural =_('Usuarios')
    
    def get_absolute_url(self):
        return "/users/%s" % self.username

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.stripe()
    
    def __str__(self):
        return f'{self.username} {self.last_name}'
    