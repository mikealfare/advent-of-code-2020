from typing import List

import pytest

from tests.conftest import day_21


sample_foods = [
    'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
    'trh fvjkl sbzzf mxmxvkd (contains dairy)',
    'sqjhc fvjkl (contains soy)',
    'sqjhc mxmxvkd sbzzf (contains fish)'
]


@pytest.fixture
def sample_food_list() -> List[day_21.Food]:
    return [day_21.parse_food(food) for food in sample_foods]


@pytest.mark.parametrize('food,expected', [
    ('mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
     day_21.Food(ingredients={'mxmxvkd', 'kfcds', 'sqjhc', 'nhms'}, allergens={'dairy', 'fish'})
     ),
    ('trh fvjkl sbzzf mxmxvkd (contains dairy)',
     day_21.Food(ingredients={'trh', 'fvjkl', 'sbzzf', 'mxmxvkd'}, allergens={'dairy'})
     ),
    ('sqjhc fvjkl',
     day_21.Food(ingredients={'sqjhc', 'fvjkl'}, allergens=None)
     )
])
def test_parse_food(food: str, expected: day_21.Food):
    assert day_21.parse_food(food) == expected


@pytest.mark.parametrize('allergen,expected', [
    ('dairy', 2),
    ('fish', 2),
    ('soy', 1)
])
def test_get_foods_with_allergen(sample_food_list, allergen, expected):
    assert len(day_21.get_foods_with_allergen(sample_food_list, allergen)) == expected


@pytest.mark.parametrize('allergen,expected', [
    ('dairy', {'mxmxvkd'}),
    ('fish', {'mxmxvkd', 'sqjhc'}),
    ('soy', {'sqjhc', 'fvjkl'})
])
def test_get_ingredients_with_allergen(sample_food_list, allergen, expected):
    assert day_21.get_ingredients_with_allergen(sample_food_list, allergen) == expected


def test_get_all_allergens(sample_food_list):
    assert day_21.get_all_allergens(sample_food_list) == {'dairy', 'fish', 'soy'}


def test_get_ingredient_to_allergen_map(sample_food_list):
    assert day_21.get_ingredient_to_allergen_map(sample_food_list) == {
        'mxmxvkd': 'dairy',
        'sqjhc': 'fish',
        'fvjkl': 'soy'
    }


def test_get_non_allergen_count(sample_food_list):
    assert day_21.get_non_allergen_count(sample_food_list) == 5
