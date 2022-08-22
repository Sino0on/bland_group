from django.contrib import admin
from django import forms

from .models import *
from ckeditor.widgets import CKEditorWidget


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm

admin.site.register(Product)
admin.site.register(Image_product)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Work)
admin.site.register(Image_work)
admin.site.register(News, NewsAdmin)
admin.site.register(Image_news)
admin.site.register(FAQ)
admin.site.register(Feedback)
admin.site.register(OrderUr)
admin.site.register(OrderFiz)
