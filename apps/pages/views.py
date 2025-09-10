from django.shortcuts import render

def error_page_view(request):
    return render(request, 'auth/404.html')

def about_page_view(request):
    return render(request, 'auth/about-us.html')

def contact_page_view(request):
    return render(request, 'auth/contact.html')

def blog_detail_page_view(request):
    return render(request, 'blogs/blog-detail.html')

def blog_list_page_view(request):
    return render(request, 'blogs/blog-list-sidebar-left.html')
