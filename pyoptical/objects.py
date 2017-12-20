from pyoptical.light_ray import lightray

class line_object:
	def __init__(self, height, position, lens_list):
		self.height = height
		self.position = position
		self._light_rays = []
		for lens in lens_list:
			_ray = lightray((position, height))
			self.add_light_ray(_ray, lens, 0)
			_ray = lightray((position, height))
			from math import pi
			self.add_light_ray(_ray, lens, 1.1)
			_ray = lightray((position, height))
			self.add_light_ray(_ray, lens, -1.1)

	def add_light_ray(self, ray, lens, angle):
		assert isinstance(ray, lightray), "Object not of type 'lightray'"
		self._light_rays.append(ray)
		_x = lens._position[0]
		from math import tan
		_y = (self.position-_x)/tan(angle) if angle != 0 else self.height
		_y2 = self.position/tan(angle) if angle != 0 else self.height
		self._light_rays[-1].add_node((_x, _y))
		if _y2 > -lens._height/2. and _y2 < lens._height/2.:
			self._light_rays[-1].add_node(lens.get_after_lens((-self.position, _y2)))
		else:
			_gradient = (_x-self.position)/(_y2+self.height)
			_inter = _y2-_gradient*_x
			print(_x, self.position, _y2, self.height, _gradient, _inter)
			self._light_rays[-1].add_node((-self.position, -self.position*_gradient+_inter))

	def show_on(self, ax):
		from matplotlib.patches import Arrow
		_object = Arrow(self.position, 0, 0, self.height, width=self.height*0.1)
		ax.add_patch(_object)
		for ray in self._light_rays:
			ray.show_on(ax)
