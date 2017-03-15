import types


class Strategy:
	def __init__(self, func=None):
		if func is not None:
			self.execute = types.MethodType(func, self)
	def execute(self):
		pass

def funcA(self):
	print "strategy A\n"

def funcB(self):
	print "strategy B\n"


if __name__ == '__main__':
	context = Strategy( funcA )
	context2 = Strategy( funcB )
	context.execute()
	context2.execute()
		