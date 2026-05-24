from django.http import HttpResponse
from django.shortcuts import redirect, render

from blog.models import Blog, Category

# Create your views here.
def posts_by_category(request,category_id):
    posts = Blog.objects.filter(category=category_id)
    #Use this when we want to do som ecustom action when category not found 
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return render(request,'404.html')
    #Use get_object_or_404 when you want to show the 404 error 
    context={
        'posts':posts,
        'category':category
    }

    return render(request,'post_category.html',context)