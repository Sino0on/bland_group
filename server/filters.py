import django_filters
from .models import Product
from .forms import ProductFilterForm


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    mini_title = django_filters.CharFilter(lookup_expr='icontains')

    # def form(self):
    #     form = ProductFilterForm
    #     return

    class Meta:
        model = Product
        fields = {'title', 'mini_title', 'category', 'subcategory'}

