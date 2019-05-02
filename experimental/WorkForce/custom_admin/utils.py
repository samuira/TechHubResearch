import re


class Util:
	first_cap_re = re.compile('(.)([A-Z][a-z]+)')
	all_cap_re = re.compile('([a-z0-9])([A-Z])')

	@staticmethod
	def convert(name):
		s1 = Util.first_cap_re.sub(r'\1_\2', name)
		return Util.all_cap_re.sub(r'\1_\2', s1).lower()
