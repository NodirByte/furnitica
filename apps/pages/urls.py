from django.urls import path

from apps.pages.views import *


app_name = 'apps.pages'

urlpatterns=[
    path('', error_page_view, name='error'),
    path('about/', about_page_view, name='about'),
    path('contact/', contact_page_view, name='contact'),
    path('blog_detail/', blog_detail_page_view, name='blog_detail'),
    path('blog_list/', blog_list_page_view, name='blog_list'),
]