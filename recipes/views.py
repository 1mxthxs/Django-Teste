from django.shortcuts import render, get_list_or_404
from utils.recipes.factory import make_recipe

from recipes.models import RecipeItem


def Home(request):
    recipes = RecipeItem.objects.filter(
        is_published=True
    ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        RecipeItem.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} |',
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
