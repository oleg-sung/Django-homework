from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe_view(request, dish):
    recipe = DATA.get(dish)
    count = int(request.GET.get('servings', 1))
    for ingredient in recipe:
        recipe[ingredient] = round((recipe[ingredient] * count), 1)
    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)


