from numpy.core.fromnumeric import sort
import requests
import numpy as np


def recipe_search(ingredient):
    app_id = '9afd0d21'
    app_key = '8fd40a5a6ef75e0c95a2d6b834d047c7'
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(
            ingredient, app_id, app_key)
    )
    data = result.json()
    return data['hits']


def run():
    dietreq = input('are you vegetarian (y/n) ')
    if dietreq == "y":
        results = recipe_search('Vegetarian')
    else:
        ingredient = input('Enter an ingredient: ')
        results = recipe_search(ingredient)

    totalWeights = []
    recipeLabels = []
    recipeUrls = []
    sort_labels = []
    sort_url = []

    choice = input("do you want recipes ordered by weight or alphabetically?")
    if choice == "weight":
        for result in results:
            recipe = result['recipe']
            totalWeights.append(recipe.get('totalWeight'))
            label = recipe['label']
            url = recipe['uri']
            recipeLabels.append(label)
            recipeUrls.append(url)

            sort_totalWeights = sorted(totalWeights)
            weight_indices = []
        for i in range(len(totalWeights)):
            index = sort_totalWeights.index(totalWeights[i])
            weight_indices.append(index)

        for i in weight_indices:
            sort_labels.append(recipeLabels[i])
            sort_url.append(recipeUrls[i])

        with open('recipes.txt', 'w+') as text_file:
            for i in range(len(sort_labels)):
                recipeWeight = str(
                sort_labels[i]) + ' weighs: ' + str(sort_totalWeights[i]) + 'g'
                text_file.write(recipeWeight + '\n')
    else:
        sortedResults = sorted(results, key=lambda x: x['recipe']['label'], reverse=False)
        file = open("recipes.txt","r+")
        file.truncate(0)
        file.close()
        for result in sortedResults:
            recipe = result['recipe']
            with open('recipes.txt', 'a') as f:
                f.writelines(''.join(recipe['label']))
                f.writelines(''.join(recipe['uri']))
                f.writelines('\n') 
run()