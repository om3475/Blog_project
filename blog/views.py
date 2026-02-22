
from django.http import HttpResponse
from django.shortcuts import render

from blogapp.models import Blog, Category

def home (request):
    featured_post = Blog.objects.filter(is_featured=True,status="Published").order_by("-updated_at")
    posts = Blog.objects.filter(is_featured=False,status="Published").order_by("-updated_at")
    context = {
        'featured_post':featured_post,
        'posts':posts,
    }

    return render(request,'home.html',context)
