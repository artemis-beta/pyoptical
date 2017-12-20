from pyoptical.light_ray import lightray

class line_object:
	def __init__(self, height, position, lens_list):
		self._height = height
		self._position = position
		self._light_rays = []
		for lens in lens_list:
			_ray = lightray((position, height))
			self.add_light_ray(_ray, lens, 0)
			_ray = lightray((position, height))
			from math import pi
			self.add_light_ray(_ray, lens, 0.1)
			_ray = lightray((position, height))
			self.add_light_ray(_ray, lens, -pi/8.)

	def add_light_ray(self, ray, lens, angle):
		assert isinstance(ray, lightray), "Object not of type 'lightray'"
		self._light_rays.append(ray)
		_x = lens._position[0]
		from math import tan
		_y = (self._position-_x)/tan(-angle) if angle != 0 else self._height
		_y2 = self._position/tan(-angle) if angle != 0 else self._height
		self._light_rays[-1].add_node((_x, _y))
		self._light_rays[-1].add_node(lens.get_after_lens((-self._position, _y2)))

	def show_on(self, ax):
		from matplotlib.patches import Arrow
		_object = Arrow(self._position, 0, 0, self._height, width=self._height*0.1)
		ax.add_patch(_object)
		for ray in self._light_rays:
			ray.show_on(ax)
