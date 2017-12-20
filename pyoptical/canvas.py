import matplotlib.pyplot as plt

class canvas:
	def __init__(self, figure_size=None, axis_x_range=(-10,10), axis_y_range=(-10,10)):
		if figure_size:
			self._f, self._ax = plt.subplots(figsize=figure_size)
		else:
			self._f, self._ax = plt.subplots()
		self._norm = True
		import numpy as np
		self._normal_line = [np.linspace(*axis_x_range, 2), np.zeros(2)]
		self._ax.set_xlim(axis_x_range)
		self._ax.set_ylim(axis_y_range)
		self._objects = []
	
	def add_object(self, item):
		self._objects.append(item)
		
	def show_normal(self, show):	
		self._norm = show

	def show(self):
		for item in self._objects:
			item.show_on(self._ax)
		if self._norm:
			plt.plot(*self._normal_line, 'r-')
		plt.show()
