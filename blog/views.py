from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Blog, Category
from django.db.models import Q

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

def single_blog(request,slug):
    blog = get_object_or_404(Blog,slug=slug)
    context={
        'blog':blog,
    }

    return render(request,'single_blog.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs= Blog.objects.filter(Q(title__icontains=keyword) |Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword))
    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)