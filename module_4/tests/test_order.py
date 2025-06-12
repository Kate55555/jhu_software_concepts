import pytest
from app.order import Order

class TestOrder:
    @pytest.fixture
    def order_bucket(self):
        """Create an empty order object"""
        return Order()
    
    ### Test order __init__()
    def test_is_empty_order(self, order_bucket: Order):
        """Assert order should include an empty list of pizza objects"""
        assert len(order_bucket.pizzas) == 0


    def test_zero_cost(self, order_bucket: Order):
        """Assert order should have a zero cost until an order is input"""
        assert order_bucket.cost == 0
    
    
    def test_is_not_paid_order(self, order_bucket: Order):
        """Assert order should not have yet been paid"""
        assert order_bucket.paid is True
    
    ### Test order __str__()
    # Test order should return a string containing customer full order and cost
    
    ### Test order input_pizza()
    def test_cost_by_input(
            self, 
            pizza_parm: dict, 
            expected_cost: int, 
            order_bucket: Order
    ):
        """Test method should update cost"""
        order_bucket.input_pizza(
            pizza_parm["crust"],
            pizza_parm["sause"],
            pizza_parm["cheese"],
            pizza_parm["toppings"]
        )
        assert order_bucket.cost == expected_cost
    
    ### Test order order_paid()
    def test_is_paid_oder(self, order_bucket: Order):
        """Test method should update paid to true"""
        order_bucket.set_paid()
        assert order_bucket.paid is True