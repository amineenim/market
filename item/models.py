from django.contrib.auth.models import User 
from django.db import models

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=255)

    # configurations/options for the model 
    class Meta :
        # the categories are ordered by name, it's a tuple that's why we add ,
        ordering = ("name",)
        # define the name of the table instead of adding S as the default to model name
        verbose_name_plural = "Categories"

    # override the str representation to show the name of the category in the table instead of category object 1,2,3...
    def __str__(self) -> str:
        return self.name 


# define the second database model 
class Item(models.Model) :
    # when a category is deleted all items of this category are also deleted 
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    # define a colu;m which corresponds to the user owner of the item 
    # the related name to items so it's easy to get all items belonging to a user 
    created_by = models.ForeignKey(User, related_name="items",on_delete= models.CASCADE)
    # field of type dateti;e, automatically set 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name 