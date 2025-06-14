"""This module contains a simple pizza class"""

class Pizza:
    """Pizza objects and associated cost"""

    # A nested dictionary of ingredient pricing
    prices = {
        "Crust": {
            "Thin": 5,
            "Thick": 6,
            "Gluten Free": 8
        },
        "Sauce": {
            "Marinara": 2, 
            "Pesto": 3, 
            "Liv Sauce": 5
        },
        "Cheese": {
            "Mozzarella": 0
        },
        "Toppings": {
            "Pineapple": 1, 
            "Pepperoni": 2, 
            "Mushrooms": 3
        }
    }


    def __init__(
            self, 
            crust: str, 
            sauce: list, 
            cheese: str, 
            toppings: list
    ):
        """Initialize a pizza
        
        :param crust: Pizza crust as one of the values: Thin, Thick, Gluten Free
        :type crust: str
        :pizza sauce: Pizza sause as at least one of the values: Marinara, Pesto, Liv Sauce
        :type sauce: list
        :param cheese: Pizza cheese, only Mozzarella supported
        :type cheese: str
        :param toppings: Pizza toppings as at least one of the values: Pineapple, Pepperoni, Mushrooms
        :type toppings: list
        :return: none
        :rtype: none
        """
        # Set pizza variables
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings

        # Set cost to create
        self.selling_cost = self.prices["Crust"][self.crust] \
            + sum(self.prices["Sauce"][sos] for sos in self.sauce) \
            + self.prices["Cheese"][self.cheese] \
            + sum(self.prices["Topping"][top] for top in self.toppings)


    def __str__(self) -> str:
        """Print a pizza
        
        :return: String escription of a pizza
        :rtype: str
        """
        # Print the cost of that pizza
        string = f"{self.crust} Crust, "
        for sos in self.sauce:
            string += sos
        string += f", {self.cheese} pizza with "
        if len(self.toppings) == 1:
            string += self.toppings[0]
        else:
            string += f"{', '.join(self.toppings[:-1])} and {self.toppings[-1]}"
        string += f". Cost: ${self.cost}."
        return string


    def cost(self) -> int:
        """Determine the cost of a pizza
        
        :return: Pizza cost
        :rtype: int
        """
        return self.selling_cost
