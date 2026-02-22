from .models import Blog, Category
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display  = ('title','category','author','is_featured','status')
    search_fields = ('title','category__category_name','status','id')
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)