from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("create", views.create, name='create'),
    path('edit/<id>/', views.edit, name='edit'),
    path('update/<id>/', views.update, name="update"),
    path('delete/<id>/', views.delete, name="delete"),

]