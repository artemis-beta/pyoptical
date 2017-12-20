class lens:
	def __init__(self, r1, r2, n, height, position=(0,0)):
		self._radius_1 = r1
		self._radius_2 = r2
		self._height = height
		self._refractive_index = n
		self._position = position
		self._focal_length = (self._refractive_index-1)*(pow(r1,-1)-pow(r2,-1))

	def get_after_lens(self, xy):
		from numpy import array
		from math import atan, tan
		x1, y1 = xy
		theta1 = atan(y1/x1)
		_tmp = array([[x1],[theta1]])*array([[1,0],[-1./self._focal_length,1]])
		_x2 = _tmp[0][0]
		_theta2 = _tmp[1][0]
		_y2 = tan(_theta2)*_x2
		return (_x2, _y2)
	
	def get_image_distance(self, object_distance):
		return pow(self._focal_length, -1) - pow(object_distance, -1)

	def get_magnification(self, object_distance):
		return -1*self.get_image_distance(object_distance)/object_distance

	def show_on(self, ax):
		import matplotlib.pyplot as plt
		x_vals = []
		y_vals = []
		try:
			_rad_1_displacement = pow(self._radius_1**2-(self._height/2.)**2, 0.5)
			_rad_2_displacement = pow(self._radius_2**2-(self._height/2.)**2, 0.5)
		
			assert not isinstance(_rad_1_displacement, complex) or not isinstance(_rad_2_displacement, complex)
		except:
			raise Exception("PYOPTICAL_LENS: Radius/Refractive Index choice leads to Complex Number coordinates, cannot perform plotting")

		from matplotlib.patches import Arc

		_lens_half_1 = Arc((self._position[0], self._position[1]), self._radius_1-_rad_1_displacement,self._height,theta1=90,theta2=270)
		_lens_half_2 = Arc((self._position[0], self._position[1]), self._radius_2-_rad_2_displacement,self._height,theta1=270,theta2=90)

		ax.add_patch(_lens_half_1)
		ax.add_patch(_lens_half_2)
