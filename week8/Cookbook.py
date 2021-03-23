#Cookbook – Recipe – Ingredient (note: recipe has 1 to many ingredients)

## Class CookBook
class CookBook:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.recipes = []
        self.names = []

    #Add recipe to CookBook
    def addRecipe(self, recipe):
        self.recipes.append(recipe)
        self.names.append(recipe.name)

    # Shows all recipes
    def showRecipes(self):
        print("All recipes in {} CookBook:".format(self.name))
        for i in self.recipes:
            print(i.name)
            
    #Print recipe with chosen name
    def getRecipe(self, name):
        index = self.names.index(name)
        print("{}'s recipe".format(self.names[index]))
        print("Ingredients:")
        for i in range(len(self.recipes[index].ingredients)):
            print("{} {} {}".format(self.recipes[index].ingredients[i].ingredient,
                                   self.recipes[index].ingredients[i].amount,
                                   self.recipes[index].ingredients[i].unit))
        print()
        print("Cooking instructions:")
        for i in range(len(self.recipes[index].steps)):
            print("{}. {}".format(i+1, self.recipes[index].steps[i]))

# Recipe Class
class Recipe:
    def __init__(self, name):
        self.name = name
        self.steps = []
        self.ingredients = []

    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)

    def addStep(self, step):
        self.steps.append(step)

# Ingredient class
class Ingredient:
    def __init__(self, ingredient, amount, unit):
        self.ingredient = ingredient
        self.amount = amount
        self.unit = unit


# Make CookBook
yumyum = CookBook('YumYum', 'Lauri Putkonen', 2021)

#Make recipe
applePie = Recipe('Burnt apple')
applePie.addStep("Burn apples in the oven")
applePie.addStep("Trash it")
apple = Ingredient('Apple', 200, 'grams')

applePie.addIngredient(apple)
yumyum.addRecipe(applePie)

#Another recipe
fruitSalad = Recipe('Fruit salad')

salad_ing1 = Ingredient("Bananas", 3, "")
fruitSalad.addIngredient(salad_ing1)
salad_ing2 = Ingredient("Grapes", 400, "grams")
fruitSalad.addIngredient(salad_ing2)
salad_ing3 = Ingredient("Kiwis", 3, "")
fruitSalad.addIngredient(salad_ing3)
salad_ing4 = Ingredient("Strawberries", 5, "dl")
fruitSalad.addIngredient(salad_ing4)

fruitSalad.addStep("Peel, Slice bananas, Kiwis and others")
fruitSalad.addStep("In large bowl, combine all ingredients, mix them gently and enjoy")

yumyum.addRecipe(fruitSalad)


# Print all recipes
yumyum.showRecipes()
print()
# Print Fruit salad
yumyum.getRecipe('Fruit salad')

#OUTPUT:
# All recipes in YumYum CookBook:
# Burnt apple
# Fruit salad

# Fruit salad's recipe
# Ingredients:
# Bananas 3 
# Grapes 400 grams
# Kiwis 3 
# Strawberries 5 dl

# Cooking instructions:
# 1. Peel, Slice bananas, Kiwis and others
# 2. In large bowl, combine all ingredients, mix them gently and enjoy




