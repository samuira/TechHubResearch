from django.shortcuts import render, render_to_response
from django.views import View
from django.utils.text import slugify
from django.contrib import messages
from .utils import Util
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ImageAnalysisForm
from .models import ImageStorage
from django.views.generic import ListView, FormView


class ImageAnalysisView(FormView):
	template_name = 'media_analysis/image_analysis.html'
	model = ImageStorage
	form_class = ImageAnalysisForm
	success_url = 'img-list/'

	def form_valid(self, form):
		image_url = ""
		analysis = Util.azure_image_analysis(image_url)

		messages.success(self.request, 'Image has been uploaded successfully.')
		return super().form_valid(form)

	def form_invalid(self, form):
		error = Util.form_validation_error(self.request, form)
		print(self.get_context_data(), error)
		self.get_context_data()['error'] = error
		return render(self.request, self.template_name)

	# def get(self, request, **kwargs):
	# 	self.context.clear()
	# 	return render(request, self.template_name, self.context)
	#
	# def post(self, request, *args, **kwargs):
	# 	print(request.POST, request.FILES)
	# 	form = self.form_class(request.POST, request.FILES)
	# 	self.context['form'] = form
	# 	print(form.is_valid())
	# 	if form.is_valid():
	# 		print(form.cleaned_data)
	# 		image_url = ""
	# 		analysis = Util.azure_image_analysis(image_url)
	# 		self.context['analysis'] = analysis
	# 		messages.success(self.request, 'Image has been uploaded successfully.')
	# 	else:
	# 		error = Util.form_validation_error(request, form)
	# 		print(self.context, error)
	# 		self.context['error'] = error
	# 	return render(request, self.template_name, self.context)


class ImageListView(ListView):
	template_name = "media_analysis/image_list.html"
	context_object_name = 'image_list'

	def get_queryset(self):
		ip = Util.get_client_ip(self.request)
		return ImageStorage.objects.filter(client_ip=ip)
