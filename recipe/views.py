from django.shortcuts import render ,redirect
from .models import new_recipe

# Create your views here.

def welcome_page(request):
    if request.method == "POST":
        data=request.POST
        recipe_name=data.get("recipe_name")
        recipe_description=data.get("recipe_description")
        recipe_image=request.FILES.get("recipe_image")

        new_recipe.objects.create(
            recipe_name=recipe_name,
            recipe_image=recipe_image,
            recipe_description=recipe_description
        )

        return redirect("/recipe/")

    return render(request,"recipe/welcome_page.html")


