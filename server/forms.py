from django import forms
from .models import *


GEEKS_CHOICES = (
    ("1", "Грунт"),
    ("2", "Песок"),
    ("3", "Асфальт"),
    ("4", "Брусчастка"),
    ("5", "Бетон"),
)
REGIONS = (
    ("1", "Чуй"),
    ("2", "Ош"),
    ("3", "Нарын"),
    ("4", "Ыссык Куль"),
    ("5", "Талас"),
    ("6", "Жалал-Абад"),
    ("7", "Баткен"),
)


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'gLTF', 'height', 'width', 'length', 'mini_title', 'material', 'category', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'height': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Высота'}),
            'width': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ширина'}),
            'length': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Длина'}),
            'mini_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Мини-название'}),
            'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Материал'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
        }


class FeedbackCreateForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш Email'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш текст', 'cols': "30", 'rows': "5"}),
        }


class OrderUrCreateForm(forms.ModelForm):
    grunt = forms.ChoiceField(choices=GEEKS_CHOICES)
    region = forms.ChoiceField(choices=REGIONS)

    class Meta:
        model = OrderUr
        fields = ['name', 'inn', 'okpo', 'bik', 'r_c', 'bank', 'director', 'adress', 'phone', 'email', 'grunt', 'region', 'text', 'city', 'delivery']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название компании'}),
            'inn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ИНН'}),
            'okpo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ОПКО'}),
            'r_c': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'р/с'}),
            'bank': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Банк'}),
            'director': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Директор'}),
            'adress': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание к заказу'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Город'}),
            'delivery': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class OrderFizCreateForm(forms.ModelForm):
    grunt = forms.ChoiceField(choices=GEEKS_CHOICES)
    region = forms.ChoiceField(choices=REGIONS)
    date_of_issue = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = OrderFiz
        fields = ['first_name', 'last_name', 'series', 'date_of_issue', 'series_type', 'adress', 'phone', 'email', 'grunt', 'region', 'text', 'city', 'delivery']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'series_type': forms.ChoiceField(attrs={'class': 'form-control', 'placeholder': 'Название компании'}),
            'inn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ИНН'}),
            'okpo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ОПКО'}),
            'r_c': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'р/с'}),
            'bank': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Банк'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Test@gmail.com'}),
            'director': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Директор'}),
            'adress': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание к заказу'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Город'}),
            'delivery': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ProductFilterForm(forms.Form):

    class Meta:
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'})
        }