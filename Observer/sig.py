# Ulysse Rémond, 2020
# Python 3.7.5
# signal of a SKS
from primitives import Prim

class Sig(Prim):
    """ Signal (Input or Output) of a Sychronous Kripke Structure """
    def __init__(self,n="DefaultSigName"):
        self.n = n #name
        self.z = False # is zero (i.e. false)

    def __nonzero__(self):
        return not self.z
