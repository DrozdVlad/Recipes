from django.contrib import admin
from recipe.models import User, Recipe


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'image', 'views']
    list_display = ('title', 'description', 'image', 'views')
