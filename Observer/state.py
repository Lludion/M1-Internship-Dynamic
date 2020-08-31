# Ulysse Rémond, 2020
# Python 3.7.5
# State of a SKS
from primitives import Prim

class State(Prim):
    """ State of a Synchronous Kripke Structure """
    def __init__(self,n=0,l={}):
        self.n = n #name, number
        self.l = l #label, labels