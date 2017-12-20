class lightray:
	def __init__(self, origin):
		self._origin = origin
		self._nodes = [origin]

	def add_node(self, coordinate):
		self._nodes.append(coordinate)

	def show_on(self, ax):
		
		_x = [i[0] for i in self._nodes]
		_y = [i[1] for i in self._nodes]
		import matplotlib.pyplot as plt
		plt.plot(_x, _y)	
