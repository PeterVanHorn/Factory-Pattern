# Factory-Pattern
Demonstration of a factory pattern in the form of a bird factory.
BirdFactory.py is the creator interface with DuckFactory.py, PigeonFactory.py and FalconFactory.py being concrete creators which extend the interface.
Bird.py is the product interface with Duck.py, Pigeon.py and Falcon.py being the concrete products.
In Main.py I create one of each type of creators, which in turn each creates one of their respective products. I then call each method of each product.
