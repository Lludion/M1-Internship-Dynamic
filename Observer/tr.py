# Ulysse Rémond, 2020
# Python 3.7.5
# transition between internal states of a SKS
from primitives import Prim
from logic import For

class Tr(Prim):
    """ (Input or Output) of a Sychronous Kripke Structure """
    def __init__(self,fr=None,to=None,B=[],out=[],tim=None):
        self.fr = fr # from this state
        self.to = to # to this state
        self.B = B # Boolean formula B(I) on the set of inputs
        self.out = out # potential output yield
        self.tim = tim # may (?) be used to get the current sychronous time
        if fr is None or to is None:
            self.n = "DefaultTr"
        else:
            self.n = str(fr.n) + "->" + str(to.n) # name

    def eval(self,context):
        tv = True # Truth value
        for b in self.B:
            if type(b) is type(For()):
                val = b.eval(context)
                #print("b",val,context)
                tv &= val
            else:
                print("\nTYPE ERROR in computing truth value of :",b,"\n")
        return tv

    def __repr__(self):
        return Prim.__repr__(self)

