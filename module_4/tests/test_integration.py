import pytest
from app.order import Order

order_bucket = Order()

@pytest.mark.order
@pytest.mark.parametrize("pizza_parm, expected_cost", [
    ({
        "crust": "Thin", "sauce": ["Marinara"], 
        "cheese": "Mozzarella", "toppings": ["Pineapple"]
    }, 5 + 2 + 1),
    ({
        "crust": "Thin", "sauce": ["Marinara", "Liv Sauce"], 
        "cheese": "Mozzarella", "toppings": ["Pepperoni", "Mushrooms"]
    }, 5 + 2 + 5 + 2 + 3),
    ({
        "crust": "Thick", "sauce": ["Pesto", "Liv Sauce"], 
        "cheese": "Mozzarella", "toppings": ["Pepperoni", "Mushrooms"]
    }, 6 + 3 + 5 + 2 + 3),
    ({
        "crust": "Gluten Free", "sauce": ["Marinara", "Pesto", "Liv Sauce"], 
        "cheese": "Mozzarella", "toppings": ["Pineapple", "Pepperoni", "Mushrooms"]
    }, 8 + 2 + 3 + 5 + 1 + 2 + 3),
])
def test_multipizza_order_cost(pizza_parm: dict, expected_cost: str):
    """Test that code can handle multiple pizza objects per order"""
    order_bucket.input_pizza(
        pizza_parm["crust"],
        pizza_parm["sauce"],
        pizza_parm["cheese"],
        pizza_parm["toppings"]
    )
    # Ensure multiple pizza objects within a given order 
    # result in an additively larger cost.
    assert order_bucket.cost == expected_cost
