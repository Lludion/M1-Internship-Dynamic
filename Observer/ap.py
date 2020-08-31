# Ulysse Rémond, 2020
# Python 3.7.5
# Atomic proposition of a SKS
from primitives import Prim

class AP(Prim):
    """ Atomic Proposition """
    def __init__(self,n="DefaultAPName"):
        self.n = n #name
