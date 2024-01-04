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


poison = Poison("Целебный отвар", 10, ["Подорожник"])
print(poison.check_description("Целебный отвар (нужно 3шт подорожник)"))  # True

poison = Poison("Приятель", 15, ["Петрушка", "Подорожник"])
print(poison.check_description("Приятель (Петрушка 1шт. и Подорожник 2шт)"))  # True

poison = Poison("Прилив сил", 20, ["Черемуха", "Петрушка", "Подорожник"])
print(poison.check_description(
    "Прилив сил (Черемуха 3шт, Петрушка 2шт, Подорожник 1шт.)"))  # True
