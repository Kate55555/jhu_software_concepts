Name: Kate Borisova (eboriso1)

Module 4 - Pytest and Sphinx

Approach: This project uses Python 3.13.2. The core .py files inculude:

I. Application source code:
app\order.py - The order class with methods to initialize, add pizzas to an order, mark as paid, and stringify.

app\pizza.py - The pizza class with methods to initialize, stringify an object, and get a pizza cost.

II. Application tests use the pytest package and are organized into the following structure:
tests\test_order.py - Tests of the Order methods.

tests\test_pizza.py - Tests of the Pizza methods.

tests\test_integration.py - Tests of Pizzas containment within Orders.

Documentation is built with Sphinx and available at https://jhu-software-concepts-module4.readthedocs.io/en/latest.

Known Bugs: None.