from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from blog.models import BlogPost
from custom_admin.models import User
from .forms import LoginForm, RegisterForm, BlogPostCreateForm
from django.shortcuts import redirect


class Dashboard(LoginRequiredMixin, View):
	template_name = 'custom_admin/dashboard.html'
	login_url = reverse_lazy('login')

	def get(self, request):
		return render(request, self.template_name)


class Login(View):
	template_name = 'custom_admin/account/login.html'
	form_class = LoginForm

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = authenticate(request=request, email=request.POST['email'], password=request.POST['password'])
			if user:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.error(request, 'Wrong email id or password.')
		return render(request, self.template_name, {'form': form})


class Register(View):
	template_name = 'custom_admin/account/register.html'
	form_class = RegisterForm

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request=request)
		if form.is_valid():
			try:
				user = User.objects.create_user(email=request.POST['email'], password=request.POST['password'])
			except ValidationError as e:
				[messages.error(request, error[0]) for error in e.message_dict.values()]
			else:
				return redirect('login')
		return render(request, self.template_name, {'form': form})


class BlogList(LoginRequiredMixin, ListView):
	template_name = 'custom_admin/blog/list.html'
	login_url = reverse_lazy('login')
	queryset = BlogPost.objects.all()
	paginate_by = 10
	context_object_name = 'blog_post'


class BlogCreate(LoginRequiredMixin, View):
	template_name = 'custom_admin/blog/create.html'
	login_url = reverse_lazy('login')
	queryset = BlogPost.objects.all()
	from_class = BlogPostCreateForm

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		form = self.from_class(request.POST, request.FILES, user=request.user)
		print(form.is_valid())
		return render(request, self.template_name)

class BlogEdit(LoginRequiredMixin, View):
	template_name = 'custom_admin/blog/edit.html'
	login_url = reverse_lazy('login')


class BlogDelete(View):
	template_name = 'custom_admin/blog/list.html'

	def get(self, request):
		return HttpResponseRedirect('/blog-list/')


class UserList(LoginRequiredMixin, View):
	template_name = 'custom_admin/user/list.html'
	login_url = reverse_lazy('login')


class UserEdit(LoginRequiredMixin, View):
	template_name = 'custom_admin/user/edit.html'
	login_url = reverse_lazy('login')

