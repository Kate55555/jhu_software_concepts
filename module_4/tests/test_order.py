import pytest
from app.order import Order

class TestOrder:
    order_bucket_1 = Order()
    order_bucket_2 = Order()


    @pytest.fixture
    def order_bucket(self):
        """Create an empty order object"""
        return Order()
    
    ### Test order __init__()
    @pytest.mark.order
    def test_is_empty_order(self, order_bucket: Order):
        """Assert order should include an empty list of pizza objects"""
        assert len(order_bucket.pizzas) == 0


    @pytest.mark.order
    def test_zero_cost(self, order_bucket: Order):
        """Assert order should have a zero cost until an order is input"""
        assert order_bucket.cost == 0
    
    
    @pytest.mark.order
    def test_is_not_paid_order(self, order_bucket: Order):
        """Assert order should not have yet been paid"""
        assert order_bucket.paid is True
    

    ### Test order __str__()
    @pytest.mark.order
    @pytest.mark.parametrize("pizza_parm, expected_str", [
        ({
            "crust": "Thin", "sauce": ["Marinara"], 
            "cheese": "Mozzarella", "toppings": ["Pineapple"]
        }, "Thin Crust, Marinara, Mozzarella pizza with Pineapple. Cost: $8."),
        ({
            "crust": "Thin", "sauce": ["Marinara", "Liv Sauce"], 
            "cheese": "Mozzarella", "toppings": ["Pepperoni", "Mushrooms"]
        }, "Thin Crust, Marinara, Mozzarella pizza with Pineapple. Cost: $8.\n \
            Thin Crust, Marinara, Liv Sauce, Mozzarella pizza with Pepperoni \
            and Mushrooms. Cost: $17."),
    ])
    def test_str(
            self, 
            pizza_parm: dict, 
            expected_str: str
    ):
        """Test order returns a string containing customer full order & cost"""
        self.order_bucket_1.input_pizza(
            pizza_parm["crust"],
            pizza_parm["sauce"],
            pizza_parm["cheese"],
            pizza_parm["toppings"]
        )
        assert str(self.order_bucket_1) == f"Customer Requested:\n {expected_str}"


    ### Test order input_pizza()
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
    def test_cost_by_input(
            self, 
            pizza_parm: dict, 
            expected_cost: int, 
            order_bucket: Order
    ):
        """Test method should update cost"""
        order_bucket.input_pizza(
            pizza_parm["crust"],
            pizza_parm["sauce"],
            pizza_parm["cheese"],
            pizza_parm["toppings"]
        )
        assert order_bucket.cost == expected_cost
    

    ### Test order order_paid()
    @pytest.mark.order
    def test_is_paid_oder(self, order_bucket: Order):
        """Test method should update paid to true"""
        order_bucket.order_paid()
        assert order_bucket.paid is True