
from django.http import HttpResponse
from django.shortcuts import render

from blogapp.models import About_us, Blog, Category

def home (request):
    featured_post = Blog.objects.filter(is_featured=True,status="Published").order_by("-updated_at")
    posts = Blog.objects.filter(is_featured=False,status="Published").order_by("-updated_at")
    about = About_us.objects.get()
    context = {
        'featured_post':featured_post,
        'posts':posts,
        'about':about,

    }

    return render(request,'home.html',context)
