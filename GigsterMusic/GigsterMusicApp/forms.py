from django import forms
from .models import *


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Product
        exclude = ("user",)


class ProductItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductItemForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():

            if (field.auto_id == 'id_product'):
                field.field.widget.attrs["class"] = "invisible"
            else:
                field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = OrderItem
        exclude = ()
        fields = {'product', 'quantity'}
        labels = {'product': '',
                  'quantity': 'Quantity'}
