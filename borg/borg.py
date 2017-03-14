class Borg(object):
	__shared_data = {}
	state1, state2 = "Idle", "Idle"
	def __init__(self):
		self.__dict__ = self.__shared_data
		self.state1 = "Running"
		self.state2 = "Running"

if __name__ == '__main__':
	obj1 = Borg()
	obj2 = Borg()
	obj1.state1 = "Dead"
	obj1.state2 = "Zombie"
	print "obj2 state1:{state1}, state2:{state2}".format(state1=obj2.state1, state2=obj2.state2)

"""
output: obj2 state1:Dead, state2:Zombie
"""
