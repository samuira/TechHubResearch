import re
from django.contrib import messages
import requests
import json


class Util:
	first_cap_re = re.compile('(.)([A-Z][a-z]+)')
	all_cap_re = re.compile('([a-z0-9])([A-Z])')

	@staticmethod
	def convert(name):
		s1 = Util.first_cap_re.sub(r'\1_\2', name)
		return Util.all_cap_re.sub(r'\1_\2', s1).lower()

	@staticmethod
	def form_validation_error(request, form):
		error = dict()
		for key in form.errors.as_data():
			if key != '__all__':
				error[key] = form.errors.as_data()[key][0].message
			else:
				messages.error(request, form.errors.as_data()[key][0].message)
		return error

	@staticmethod
	def azure_image_analysis(image_url):
		subscription_key = "d6d01d04272b4927bdae599739b83a23"
		vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
		analyze_url = vision_base_url + "analyze"
		image_url = "https://www.terra.uliege.be/upload/docs/image/png/2018-05/agriculture-is-life-large.png"
		headers = {'Ocp-Apim-Subscription-Key': subscription_key}
		params = {'visualFeatures': 'Categories,Description,Color'}
		data = {'url': image_url}
		response = requests.post(analyze_url, headers=headers, params=params, json=data)
		response.raise_for_status()
		return response.json()

	@staticmethod
	def get_client_ip(request):
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
		return ip
