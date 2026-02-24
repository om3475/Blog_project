
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .form import registration_form
from blogapp.models import Blog, Category
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate ,login, logout 


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

def registration(request):
    if request.POST:
        form = registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration')
        return render(request,'registration.html',{'form':registration_form()}) 
    else:
        form = registration_form()
        context ={
            'form':form
        }
     
    
        return render(request,'registration.html',context) 
def user_login(request):
    if request.POST:
        form = AuthenticationForm(request,request.POST)
        if  form.is_valid():
            login(request,form.get_user())
            return redirect('home')       
        return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request,'login.html',context)
def user_logout(request):
    logout(request)
    return redirect('login')