def cakes(recipe, available):
    
    recipeKeys = list(recipe.keys())
    availableKeys = list(available.keys())

    for recipeKey in recipeKeys:
        if availableKeys.count(recipeKey) < 1:
            return 0
    
    lst = []
    for meterial in recipe:
        lst.append(int(available[meterial]/recipe[meterial]))
            
    return min(lst)