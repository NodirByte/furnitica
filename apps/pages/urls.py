from django.urls import path

from apps.pages.views import *


app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('error/', error_page_view, name='error'),
    path('about/', about_page_view, name='about'),
    path('contact/', contact_page_view, name='contact'),
    path('blog/', blog_list_page_view, name='blog_list'),
    path('blog/detail/', blog_detail_page_view, name='blog_detail'),
    path('products/', product_grid_view, name='product_grid'),
    path('products/detail/', product_detail_view, name='product_detail'),
    path('cart/', product_cart_view, name='cart'),
    path('checkout/', product_checkout_view, name='checkout'),
    path('login/', user_login_view, name='login'),
    path('register/', user_register_view, name='register'),
    path('reset-password/', user_reset_password_view, name='reset_password'),
    path('account/', user_account_view, name='account'),
    path('wishlist/', user_wishlist_view, name='wishlist'),
]
