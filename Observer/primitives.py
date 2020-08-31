# Ulysse Rémond, 2020
# Python 3.7.5
# Primitives for objects in this project

class Prim:
	def __repr__(self):
		return self.__class__.__name__ + " : " + self.n

	def __hash__(self):
		return hash(self.n)

	def __eq__(self, other):
		return self.n == other.n