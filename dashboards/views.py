from django.shortcuts import get_object_or_404, redirect, render

from blogapp.models import Blog, Category
from django.contrib.auth.decorators import login_required

from dashboards.forms import Add_blog_form, Category_form, EditUserForm,AddUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your views here.

@ login_required(login_url='login')
def dashboard(request):
 category_count = Category.objects.all().count()
 blog_count = Blog.objects.all().count()

 context = {
  'category_count':category_count,
  'blog_count':blog_count

 }
 return render(request,"dashboards/dashboard.html",context)
# CATEGORIES CURD
def categories (request):
 return render(request,'dashboards/categories.html')

def add_category(request) :
    if request.method == 'POST':
        form = Category_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = Category_form()
    context = {
    'form':form,
    }

    return render (request,'dashboards/add_category.html',context)

def edit_category(request,pk) :
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = Category_form(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        
        form = Category_form(instance=category)
        context = {
        'form':form,
        'category':category,
        }

        return render (request,'dashboards/edit_category.html',context)

def delete_category(request,pk) :
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect ('categories')

# BLOGS CURD
def posts(request):
   posts = Blog.objects.all().order_by('-updated_at')
   context = {
      'posts':posts,
   }
   return render(request,'dashboards/posts.html',context)

def add_blog(request):
   
    if request.method=="POST":
      form = Add_blog_form(request.POST,request.FILES)
      if form.is_valid():
        post = form.save(commit=False) #temporarily saving
        post.author = request.user
        post.save()
        title = form.cleaned_data['title']
        post.slug = slugify(title)+'-'+str(post.id)
        post.save()
        return redirect('posts')
      else:
         return render(request,'dashboards/add_blog.html',{'form':form}) 
        
    else:
     form = Add_blog_form()
     context = {
        'form':form,
     }
     return render(request,'dashboards/add_blog.html',context) 

def edit_blog(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method=="POST":
      form = Add_blog_form(request.POST,request.FILES, instance=blog)
      if form.is_valid():
        
        post = form.save()
        title = form.cleaned_data['title']
        post.slug = slugify(title)+'-'+str(post.id)
        post.save()
        return redirect('posts')
      else:
         return render(request,'dashboards/edit_blog.html',{'form':form}) 
        
    else:
    
     form = Add_blog_form(instance=blog)
     context = {
        'form':form,
        'blog':blog,

     }
     return render(request,'dashboards/edit_blog.html',context) 
    
def delete_blog (request,pk):
    blog =get_object_or_404(Blog,pk=pk,author=request.user)
    blog.delete()
    return redirect('posts')

def users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'dashboard/users.html', context)


def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = AddUserForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_user.html', context)


def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/edit_user.html', context)


def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')