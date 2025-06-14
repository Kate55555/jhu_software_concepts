import pytest
from app.pizza import Pizza

### Test pizza __init__()

@pytest.fixture
def create_pizza(self):
    """Pizza initializer"""
    return Pizza("Thin", ["Marinara"], 
                "Mozzarella", ["Pineapple"])


def test_pizza_init(self, create_pizza: Pizza):
    """Test return an initialized pizza"""
    assert isinstance(create_pizza, Pizza)


@pytest.mark.parametrize("attr, expected_type", [
    (getattr(create_pizza, "crust"), str),
    (getattr(create_pizza, "sauce"), list),
    (getattr(create_pizza, "cheese"), str),
    (getattr(create_pizza, "toppings"), list),
])
def test_pizza_attrs(
        attr: list | str, 
        expected_type: str
):
    """Test pizza should have crust (str), sauce (list of str), 
    cheese (str), toppings (list of str)"""
    if isinstance(attr, list):
        assert all(isinstance(x, str) for x in attr)
    assert isinstance(attr, expected_type)


def test_pizza_non_zero_cost(self, pizza: Pizza):
    """Test pizza should return a non-zero cost"""
    assert pizza.cost() != 0


### Test pizza __str__()
@pytest.mark.parametrize("pizza_parm, expected_str", [
    ({
        "crust": "Thin", "sauce": ["Marinara"], 
        "cheese": "Mozzarella", "toppings": ["Pineapple"]
    }, "Thin Crust, Marinara, Mozzarella pizza with Pineapple. Cost: $8."),
    ({
        "crust": "Thin", "sauce": ["Marinara", "Liv Sauce"], 
        "cheese": "Mozzarella", "toppings": ["Pepperoni", "Mushrooms"]
    }, "Thin Crust, Marinara, Liv Sauce, Mozzarella pizza with Pepperoni \
        and Mushrooms. Cost: $17."),
    ({
        "crust": "Thick", "sauce": ["Marinara", "Pesto", "Liv Sauce"], 
        "cheese": "Mozzarella", "toppings": ["Pineapple", "Pepperoni", "Mushrooms"]
    }, "Thick Crust, Marinara, Pesto, Liv Sauce, Mozzarella pizza with \
        Pineapple, Pepperoni and Mushrooms. Cost: $22."),
])
def test_str(pizza_parm: dict, expected_str: str):
    """Test pizza should return a string containing the pizza and cost"""
    pizza = Pizza(
        pizza_parm["crust"],
        pizza_parm["sauce"],
        pizza_parm["cheese"],
        pizza_parm["toppings"]
    )
    assert str(pizza) == expected_str


### Test pizza cost()
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
def test_pizza_cost(pizza_parm: dict, expected_cost: int
):
    """Test return of correct cost for an input pizza"""
    pizza = Pizza(
        pizza_parm["crust"],
        pizza_parm["sauce"],
        pizza_parm["cheese"],
        pizza_parm["toppings"]
    )
    assert pizza.cost() == expected_cost