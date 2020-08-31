# Ulysse Rémond, 2020
# Python 3.7.5
# Logic with timed variables
from primitives import Prim

class For(Prim):
    def __init__(self,l=None,r=None,op=None):
        """ For is short for Formula """
        self.l = l # left, can be "NOT"
        self.r = r # right
        self.n = "<"+str(self.l)+'~'+str(self.r)+'>' # name

    def eval(self,context):
        """ Evaluates recursively the For object in the given context """
        if self.r is None:
            if self.l is None:
                return False
            else:
                return self.__evalbranch(self.l,context)
        else:
            if self.l is None:
                return self.__evalbranch(self.r,context)
            else:
                if type(self.l) == type(""):
                    if self.l.lower() != "not":
                        print("Unclear command, interpreted as 'not'.")
                    return not self.__evalbranch(self.r,context)

                else:
                    return self.__evalbranch(self.l,context) or self.__evalbranch(self.r,context)


    def __evalbranch(self,branch,context):
        if type(branch) == type(self):
            return branch.eval(context)
        else: # is a leaf
            if type(branch) == type(""):
                print("Incorrect leaf.")
            return branch in context
