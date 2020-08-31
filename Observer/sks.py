# Ulysse Rémond, 2020
# Python 3.7.5
# Synchronous Kripke Structure
from primitives import Prim
from ap import AP
from state import State
from sig import Sig
from tr import Tr
from logic import For

class Sks(Prim):
    """ Sychronous Kripke Structure """
    def __init__(self,A={AP("unsafe")},S={State("s0")},s=State("s0"),I={Sig("in")},O={Sig("out")},R=[Tr()],L=lambda x:x):
        self.A = A # atomic propositions (names)
        self.S = S # states (names)
        self.s = s # current state (belongs to S)
        self.I = I # inputs (names)
        self.O = O # outputs (names) so that no element is in I and O
        self.R = R # transition relation (S x B (I(t)) x P(O) x S )
        self.L = L # labeling function
        self.id = id(self)

    def update(self,inputs=[]):
        self.__checkinputs(inputs)
        for tr in self.R:
            if tr.fr == self.s:
                #print("PROCESSING ",tr)
                if tr.eval(inputs):
                    self.s = tr.to # updating state
                    print("TAKING ",tr)
                    print("CURRENT OUTPUT : ",tr.out)
                    return

    def __checkinputs(self,inputs):
        for i in inputs:
            if i not in self.I:
                print("--WARNING-- Unknown input : ",i)

    def __repr__(self):
        contents = "\nAP: " +  str(self.A)
        contents += "\nS: " +  str(self.S)
        contents += "\nI: " +  str(self.I)
        contents += "\nO: " +  str(self.O)
        contents += "\nR: " +  str(self.R)
        contents += "\nL: " +  str(self.L)
        return "Sks n°" + str(self.id) + " in " + str(self.s) + " :" + contents


##

#Controller model
#lowering the barrier
tr1 = Tr(State("s0"),State("s1"),[For(Sig("inI"),Sig("inR"))],[Sig("lower")])

#raising the barrier
tr2 = Tr(State("s1"),State("s0"),[For(Sig("exited"))],[Sig("raise")])

IimplR = For(Sig("inR"),For("NOT",Sig("inI")))
EXimplI = For(For("NOT",Sig("exited")),Sig("inI"))
maili = [IimplR,EXimplI]

#a bug
tr3 = Tr(State("s1"),State("s1"),maili,[])

conTran = [tr3,tr2,tr1]

def f(x):
    assert x.n == "s0" or x.n == "s1"
    if x.n == "s0":
        x.l = AP("RAISE")
        return AP("RAISE")
    elif x.n == "s1":
        x.l = AP("LOWER")
        return AP("LOWER")

control = Sks(A={AP("LOWER"),AP("RAISE")},S={State("s0"),State("s1")},s=State("s0"),I={Sig("inR"),Sig("inI"),Sig("exited")},O={Sig("raise"),Sig("lower")},R=conTran,L=f)

#Plant model
plant = Sks(A={AP("DOWN"),AP("UP"),AP("GOINGDOWN"),AP("GOINGUP")},S={State("s0"),State("s1"),State("s2"),State("s3")},s=State("s0"),I={Sig("raise"),Sig("lower")},O={Sig("down"),Sig("up"),Sig("goingdown"),Sig("goingup")},R=[],L=f)

#Observer FB
obs = Sks(A={AP("Violation")},S={State("s0"),State("s1")},s=State("s0"),I={Sig("inR"),Sig("inI"),Sig("exited")},O={Sig("raise"),Sig("lower")},R=conTran,L=f)

##
#testing the formula & updates

incoming = [Sig("inR"),Sig("inI")]
end = [Sig("exited")]

