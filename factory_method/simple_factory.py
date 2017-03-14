class A:
	def dump(self):
		print "dump class A"

class B:
	def dump(self):
		print "dump class B"

def get_factory(factory='A'):
	factories = dict(A=A, B=B)
	return factories[factory]()

a, b = get_factory("A"), get_factory("B")
a.dump()
b.dump()