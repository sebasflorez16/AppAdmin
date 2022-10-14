import code
from enum import unique
from secrets import choice
from tabnanny import verbose
from django.db import models
from bases_app.models import BaseModel
from simple_history.models import HistoricalRecords
# Create your models here.


TYPE_OF_PERSON=(
    ('Natural', 'Natural'),
    ('Juridica', 'Juridica'),
)



# Modulo para ventas

class Clients(BaseModel):
    dni = models.IntegerField(max_length=100)
    first_name = models.CharField(max_length=100, verbose_name="Nombre Completo")
    last_name = models.CharField(max_length=100, verbose_name="Apellidos")
    phone = models.IntegerField(max_length=100)
    email = models.EmailField(blank=True, null=True, max_length=100)
    address = models.CharField()
    historical = HistoricalRecords()

    #Maneja el historial de los usuarions que han hecho cambios

    @property
    def _history_user(self):  #Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value


    class Meta:
        verbose_name = 'Cliente'
    
    def __str__(self):
        return self.first_name
        
# Modulo reservado para compras
class Business(BaseModel):
    code = models.AutoField(primary_key=True, unique=True, 
                                help_text="Es el identicador de la empresa en nuestro sistema")
    business = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=20) 
    address = models.CharField(max_length=100, verbose_name='Direccion de la empresa')
    email = models.EmailField()
    historical = HistoricalRecords()


    @property
    def _history_user(self):  #Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value


    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        
    def __str__(self):
        return self.name




class Providers(BaseModel):
    code = models.AutoField(primary_key=True, unique=True, 
                                help_text="Es el identicador del Proveedor en nuestro sistema")
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type_of_person = models.CharField(choice=TYPE_OF_PERSON, verbose_name="Tipo de Persona",
                                help_text="Mencione el estasdo tributario si es natural o juridico")
    name = models.CharField(max_length=100, verbose_name="Nombre",
                                help_text="El nombre de la empresa o si es independiente")
    address = models.CharField(max_lenhth=100, verbose_name="Direccion de la empresa")
    phone = models.IntegerField(max_length=59, verbose_name="Telefono")
    post_code = models.IntegerField(max_length=10, null=True, blank=True, verbose_name="Codigo Postal")
    email = models.EmailField(max_length=100)
    historical = HistoricalRecords()

    @property
    def _history_user(self):  #Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value


    class Meta:
        verbose_name = 'Provedor'
        verbose_name_plural = 'Provedores'
        
    def __str__(self):
        return self.int(code)

        


