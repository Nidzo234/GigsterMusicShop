from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Product
        exclude = ("user",)


class OrderInformationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderInformationForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = OrderInformation
        exclude = ("user", "date",)


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


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
