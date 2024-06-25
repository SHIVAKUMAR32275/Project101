from django.urls import path
from .import views

urlpatterns=[
    path("recipe/",views.welcome_page,name="main_page")
]