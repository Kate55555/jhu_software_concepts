"""This module contains an order class"""
from src.pizza import Pizza

class Order:
    """Order object and associated pizzaz and total cost"""
    def __init__(self):
        """Initialize a customer order

        :return: none
        :rtype: none
        """
        # Initialize order cost
        self.cost = 0
        # Initialize as an unpaid order
        self.paid = False
        # Initialize empty order
        self.pizzas = []


    def __str__(self) -> str:
        """Print a customer's complete order

        :return: Order details, including pizzas and costs
        :rtype: str
        """
        string = "Customer Requested:\n"
        for i in range(len(self.pizzas)):
            string += f"{str(self.pizzas[i])}\n"
        return string


    def input_pizza(
            self, 
            crust: str, 
            sauce: list, 
            cheese: str, 
            toppings: list
    ):
        """Input the customer's order for a given pizza
        
        :param crust: Pizza crust as one of the values: Thin, Thick, Gluten Free
        :type crust: str
        :param sauce: Pizza sause as at least one of the values: Marinara, Pesto, Liv Sauce
        :type sauce: list
        :param cheese: Pizza cheese, only Mozzarella supported
        :type cheese: str
        :param toppings: Pizza toppings as at least one of the values: Pineapple, Pepperoni, Mushrooms
        :type toppings: list
        :return: none
        :rtype: none
        """
        # Initialize the pizza object and attach to the order
        pizza = Pizza(crust, sauce, cheese, toppings)
        self.pizzas.append(pizza)

        # Update the cost
        self.cost += pizza.cost()


    def order_paid(self):
        """Set order as paid once payment has been closed

        :return: none
        :rtype: none
        """
        self.paid = True
