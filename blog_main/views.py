from django.shortcuts import render

from blog.models import Blog, Category 

def home(request):
    
    featured_posts = Blog.objects.filter(featured=True).order_by('-updated_at')
    posts = Blog.objects.filter(featured=False)
    context = {
        
        'featured_posts':featured_posts,
        'posts':posts
        
    }
    return render(request,'home.html',context)