from tkinter import Widget
from django import forms


from .models import *


class MaeasureUnitForm(forms.ModelForm):
    class Meta:
        model = MeasureUnit
        fields = ['description', 'state' ]
        labels = {'description': 'Descripcion de la Unidad de Medida', 
                    'state':'Estado de al Categoria'}
        widget ={'description': forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.field):
                self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class CategoryProductForm(forms.ModelForm):
    class Meta:
        model = CategoryProduct
        fields = ['description', 'state']
        labels = {'description': 'Descripción de la Categoria',
                    'state':'Estado Actual'}
        widget = {'description': forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.field):
                self.fields[field].widget.attrs.update({
                'class':'form-control'
            }) 
class IndicatorForm(forms.ModelForm):
    class Meta:
        model = Indicator
        fields = ['descount_value', 'category_product', 'description','state']
        labels = {'descount_value': 'Valor de descuento',
                     'category_product':'Categoria',
                     'description':'Descripción',
                     'state':'Estado'}
        widget = {'description': forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.field):
                self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'measure_unit', 'category_product',
                    'image', 'quantity', 'state' ]
        labels = {'name': 'Nombre', 'description': 'Descripción', 'measure_unit': 'Unidad de Medida', 'category_product': 'Categoria del Producto',
                    'image':'Imagen', 'quantity':'Cantidad', 'state':'Estado'}






