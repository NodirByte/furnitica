from django.shortcuts import render
from django.contrib import messages


def home_page_view(request):
    return render(request, 'home3.html')


def error_page_view(request):
    return render(request, 'auth/404.html')


def about_page_view(request):
    return render(request, 'auth/about-us.html')


def contact_page_view(request):
    if request.method == 'POST':
        messages.success(request, 'Your message has been sent successfully!')
    return render(request, 'auth/contact.html')


def blog_detail_page_view(request):
    return render(request, 'blogs/blog-detail.html')


def blog_list_page_view(request):
    return render(request, 'blogs/blog-list-sidebar-left.html')


def product_grid_view(request):
    return render(request, 'products/product-grid-sidebar-left.html')


def product_detail_view(request):
    return render(request, 'products/product-detail.html')


def product_cart_view(request):
    return render(request, 'products/product-cart.html')


def product_checkout_view(request):
    return render(request, 'products/product-checkout.html')


def user_login_view(request):
    return render(request, 'user/user-login.html')


def user_register_view(request):
    return render(request, 'user/user-register.html')


def user_reset_password_view(request):
    return render(request, 'user/user-reset-password.html')


def user_account_view(request):
    return render(request, 'user/user-acount.html')


def user_wishlist_view(request):
    return render(request, 'user/user-wishlist.html')

