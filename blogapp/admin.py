from .models import About_us, Blog, Category, Social
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display  = ('title','category','author','is_featured','status')
    search_fields = ('title','category__category_name','status','id')
    list_editable = ('is_featured',)

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About_us.objects.all().count()
        if count == 0:
            return True
        else:
            return False
        
# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(About_us,AboutAdmin)
admin.site.register(Social)

