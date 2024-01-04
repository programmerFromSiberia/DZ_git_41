class Poison:
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients

    def check_description(self, description):
        required_ingredients = description.split(
            " (")[1].split(")")[0].split(", ")
        for ingredient in required_ingredients:
            if ingredient not in self.ingredients:
                return False
        return True


class PotionEditor:
    def create_potion(self):
        name = input("Enter the name of the potion: ")
        cost = int(input("Enter the cost of the potion: "))

        ingredients_str = input(
            "Enter the required ingredients for the potion (separated by commas): ")
        ingredients = [ingredient.strip()
                       for ingredient in ingredients_str.split(",")]

        potion = Poison(name, cost, ingredients)
        return potion

    def edit_potion(self, potion):
        print("Current name: ", potion.name)
        new_name = input(
            "Enter the new name of the potion (leave blank if no change): ")
        if new_name:
            potion.name = new_name

        print("Current cost: ", potion.cost)
        new_cost = input(
            "Enter the new cost of the potion (leave blank if no change): ")
        if new_cost:
            potion.cost = int(new_cost)

        print("Current ingredients: ", potion.ingredients)
        new_ingredients_str = input(
            "Enter the new required ingredients for the potion (leave blank if no change): ")
        if new_ingredients_str:
            new_ingredients = [ingredient.strip()
                               for ingredient in new_ingredients_str.split(",")]
            potion.ingredients = new_ingredients

        return potion


editor = PotionEditor()
potion1 = editor.create_potion()
print(potion1.name, potion1.cost, potion1.ingredients)

potion2 = editor.edit_potion(potion1)
print(potion2.name, potion2.cost, potion2.ingredients)
