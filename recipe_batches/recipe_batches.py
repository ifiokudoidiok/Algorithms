#!/usr/bin/python

import math

# def recipe_batches(recipe, ingredients):
#   pass 
def recipe_batches(recipe, ingredients):
  # create a variable where we keep track of the 'how many times'
  how_many_times = []
  # if recipe length is longer than ingredients length:
  if len(recipe) > len(ingredients):
    # return 0
    return 0
  # for loop which loops over all keys from recipe
  for key in recipe:
    # if checks if the all keys from the recipes exist in ingredients
    if key not in ingredients:
      # if not we return 0
      return 0
    else:
      # we append ingredients item // recipe item to how many times var
      how_many_times.append(ingredients[key] // recipe[key])
  # we return the min value from how many times variable
  return min(how_many_times)
# O(n)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))