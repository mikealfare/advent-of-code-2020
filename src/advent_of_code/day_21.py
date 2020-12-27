from typing import Set, Optional, List, Dict
from dataclasses import dataclass


@dataclass
class Food:
    ingredients: Set[str]
    allergens: Optional[Set[str]]


def get_foods_with_allergen(foods: List[Food], allergen: str) -> List[Food]:
    foods_with_allergen = []
    for food in foods:
        if allergen in food.allergens:
            foods_with_allergen.append(food)
    return foods_with_allergen


def get_ingredients_with_allergen(foods: List[Food], allergen: str) -> Set[str]:
    foods_with_allergen = get_foods_with_allergen(foods, allergen)
    ingredients = foods_with_allergen[0].ingredients
    for i in range(1, len(foods_with_allergen)):
        ingredients = ingredients.intersection(foods_with_allergen[i].ingredients)
    return ingredients


def get_all_allergens(foods: List[Food]) -> Set[str]:
    allergens = set()
    for food in foods:
        allergens = allergens.union(food.allergens)
    return allergens


def identify_ingredient_for_each_allergen(potential_ingredients: Dict[str, Set[str]]) -> Dict[str, str]:
    while True:
        identified_ingredients = set()
        for ingredients in potential_ingredients.values():
            if len(ingredients) == 1:
                identified_ingredients = identified_ingredients.union(ingredients)
        for allergen, ingredients in potential_ingredients.items():
            if len(ingredients) > 1:
                potential_ingredients.update({allergen: ingredients - identified_ingredients})
        ingredient_counts = {len(ingredients) for ingredients in potential_ingredients.values()}
        if ingredient_counts == {1}:
            ingredient_map = {}
            for allergen, ingredients in potential_ingredients.items():
                ingredient = ingredients.pop()
                ingredient_map.update({ingredient: allergen})
            return ingredient_map


def get_ingredient_to_allergen_map(foods: List[Food]) -> Dict[str, str]:
    allergens = get_all_allergens(foods)
    potential_ingredients = {}
    for allergen in allergens:
        ingredients = get_ingredients_with_allergen(foods, allergen)
        potential_ingredients.update({allergen: ingredients})
    return identify_ingredient_for_each_allergen(potential_ingredients)


def get_non_allergen_count(foods: List[Food]) -> int:
    allergen_ingredients = get_ingredient_to_allergen_map(foods)
    non_allergen_count = 0
    for food in foods:
        non_allergen_count += len(food.ingredients - allergen_ingredients.keys())
    return non_allergen_count


def parse_food(food: str) -> Food:
    food = food.replace('(', '').replace(')', '')
    ingredients = food.split('contains')[0]
    ingredient_list = set(ingredients.strip().split(' '))
    if 'contains' in food:
        allergens = food.split('contains')[1]
        allergen_list = {allergen.strip() for allergen in allergens.split(',')}
    else:
        allergen_list = None
    return Food(ingredients=ingredient_list, allergens=allergen_list)


def main():
    with open('input_files/day_21.txt') as f:
        foods = [parse_food(line.strip()) for line in f.readlines()]
    print(f'non-allergen ingredients appear {get_non_allergen_count(foods)} times')
    ingredient_to_allergen = get_ingredient_to_allergen_map(foods)
    sorted_ingredients = [i for i, _ in sorted(ingredient_to_allergen.items(), key=lambda x: x[1])]
    print(f'the dangerous ingredient list is {",".join(sorted_ingredients)}')


if __name__ == '__main__':
    main()
