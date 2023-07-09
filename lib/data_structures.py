spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [nam["name"] for nam in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    names = [nam for nam in spicy_foods if nam["heat_level"] > 5]
    return names

def print_spicy_foods(spicy_foods):
    for cuisine in spicy_foods:
        print(
            f"{cuisine['name']} ({cuisine['cuisine']}) | Heat Level: {'🌶' * cuisine['heat_level']}"
        )

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for meal in spicy_foods:
        if cuisine == meal["cuisine"]:
            return meal

def print_spiciest_foods(spicy_foods):
    for cuisine in spicy_foods:
        if cuisine["heat_level"] > 5:
            print(
                f"{cuisine['name']} ({cuisine['cuisine']}) | Heat Level: {'🌶' * cuisine['heat_level']}"
            )

def get_average_heat_level(spicy_foods):
    avg_heat_level = sum([cuisine["heat_level"] for cuisine in spicy_foods]) / len(spicy_foods)
    return avg_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    cuisine_list = spicy_foods
    cuisine_list.append(spicy_food)
    return cuisine_list
