
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from blogapp.models import Blog, Category
from django.db.models import Q

# Create your views here.
def blog_by_category(request,category_id):
    posts = Blog.objects.filter(status = "Published",category = category_id)
  
    category_name = Category.objects.get(pk = category_id)

    context = {
        'posts':posts,
        'category_name':category_name,

    }
    return render(request,'blog_by_category.html',context)

def single_blog(request,slug):
    single_blog = get_object_or_404(Blog,slug=slug,status ='Published')
    context = {
        'single_blog':single_blog,
    }
    return render(request,'single_blog.html',context)

def search_blog(request):
    keyword =request.GET.get("search")
    print(keyword)
    searched_blogs = Blog.objects.filter(Q(title__icontains =keyword) | Q(short_discription__icontains =keyword) | Q(blog_body__icontains =keyword),status = "Published") 
    context = {
     'searched_blogs':searched_blogs,
     'keyword':keyword
   }
    return render(request,'search.html',context)