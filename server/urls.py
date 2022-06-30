from django.urls import path, re_path
from .views import *
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', index, name='home'),
    path('product', product_list, name='product_list'),
    path('delete/<int:id>', postdelete, name='delete'),
    path('news', news_list, name='news'),
    path('product_create', product_create, name='product_create'),
    # path('product_detail/<int:pk>', product_detail, name='product_detail'),
    path('components', components),
    path('orders', orders, name='orders'),
    path('test', test),
    path('register', register, name='register'),
    path('login', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('cart', cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
    path('orderfiz_create', orderfiz_create, name='orderfiz'),
    path('orderur_create', orderur_create, name='orderur'),
    # path('word', get_document, name='word'),
]