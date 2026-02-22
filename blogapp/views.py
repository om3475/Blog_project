
from django.http import HttpResponse
from django.shortcuts import render

from blogapp.models import Blog, Category

# Create your views here.
def blog_by_category(request,category_id):
    posts = Blog.objects.filter(status = "Published",category = category_id)
  
    category_name = Category.objects.get(pk = category_id)

    context = {
        'posts':posts,
        'category_name':category_name,

    }
    return render(request,'blog_by_category.html',context)