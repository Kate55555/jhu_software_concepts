import pytest
from app.pizza import Pizza

class TestPizza:
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
        self, 
        attr: list | str, 
        expected_type: str
    ):
        """Test pizza should have crust (str), sauce (list of str), 
        cheese (str), toppings (list of str)"""
        if isinstance(attr, list):
            assert all(isinstance(x, str) for x in attr)
        assert isinstance(attr, expected_type)


    # Test pizza should return a non-zero cost

    ### Test pizza __str__()
    # Test pizza should return a string containing the pizza and cost

    ### Test pizza cost()
    # Test return of correct cost for an input pizza
    pass