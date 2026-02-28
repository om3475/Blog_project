from django.urls import  path
from . import views
urlpatterns = [
    path('',views.dashboard,name = 'dashboard'),
    path('/categories/',views.categories,name = 'categories'),
    path('/add/',views.add_category,name = 'add_category'),
    path('/edit/<int:pk>/',views.edit_category,name = 'edit_category'),
    path('/delete/<int:pk>/',views.delete_category,name = 'delete_category'),






]