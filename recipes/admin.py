from django.contrib import admin

from .models import Category, RecipeItem


class CategoryAdmin(admin.ModelAdmin):
    admin.site.register(Category)


class RecipeItemAdmin(admin.ModelAdmin):
    admin.site.register(RecipeItem)
