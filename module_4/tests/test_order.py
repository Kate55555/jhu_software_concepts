import pytest
from app.order import Order

class TestOrder:
    def order_bucket(self):
        """Create an empty order object"""
        return Order()
    
    ### Test order __init__()
    def test_is_empty_order(self, empty_order: Order):
        """Assert order should include an empty list of pizza objects"""
        assert len(empty_order.pizzas) == 0


    def test_zero_cost(self, empty_order: Order):
        """Assert order should have a zero cost until an order is input"""
        assert empty_order.cost == 0
    
    
    def test_is_paid_order(self, empty_order: Order):
        """Assert order should not have yet been paid"""
        assert empty_order.ispaid is True
    
    ### Test order __str__()
    # Test order should return a string containing customer full order and cost
    
    ### Test order input_pizza()
    # Test method should update cost
    
    ### Test order order_paid()
    # Test method should update paid to true
    pass