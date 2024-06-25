from django.db import models


# Create your models here.


class new_recipe(models.Model):
    recipe_name=models.CharField(max_length=100)
    recipe_description=models.TextField()
    recipe_image=models.ImageField(upload_to="recipe_folder")



