from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView
from blog.models import BlogPost
from custom_admin.models import User
from custom_admin.utils import Util
from .forms import LoginForm, RegisterForm, BlogPostCreateForm, BlogPostEditForm, UserEditForm
from django.shortcuts import redirect


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
	template_name = 'custom_admin/dashboard.html'
	login_url = reverse_lazy('login')

	def test_func(self):
		return self.request.user.is_superuser

	def handle_no_permission(self):
		messages.error(self.request, 'Permission denied!!!')
		return redirect('login')

	def get(self, request):
		return render(request, self.template_name)


class Login(View):
	template_name = 'custom_admin/account/login.html'
	form_class = LoginForm
	context = dict()

	def get(self, request, *args, **kwargs):
		self.context.clear()
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		self.context.clear()
		form = self.form_class(request.POST)
		self.context['form'] = form
		if form.is_valid():
			user = authenticate(request=request, email=request.POST['email'], password=request.POST['password'])
			if user:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.error(request, 'Incorrect Email or Password')
		else:
			error = Util.form_validation_error(request, form)
			self.context['error'] = error
		return render(request, self.template_name, self.context)


class Register(View):
	template_name = 'custom_admin/account/register.html'
	form_class = RegisterForm
	context = dict()

	def get(self, request, *args, **kwargs):
		self.context.clear()
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		self.context.clear()
		form = self.form_class(request.POST, request=request)
		self.context['form'] = form
		if form.is_valid():
			try:
				user = User.objects.create_user(email=request.POST['email'], password=request.POST['password'])
			except ValidationError as e:
				[messages.error(request, error[0]) for error in e.message_dict.values()]
			else:
				return redirect('login')
		else:
			error = Util.form_validation_error(request, form)
			self.context['error'] = error

		return render(request, self.template_name, self.context)


class Logout(LoginRequiredMixin, UserPassesTestMixin, View):
	login_url = reverse_lazy('login')

	def test_func(self):
		return self.request.user.is_superuser

	def handle_no_permission(self):
		messages.error(self.request, 'Permission denied!!!')
		return redirect('login')

	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('login'))


class BlogList(LoginRequiredMixin, UserPassesTestMixin, ListView):
	template_name = 'custom_admin/blog/list.html'
	login_url = reverse_lazy('login')
	queryset = BlogPost.objects.all()
	paginate_by = 10
	context_object_name = 'blog_post'

	def test_func(self):
		return self.request.user.is_superuser

	def handle_no_permission(self):
		messages.error(self.request, 'Permission denied!!!')
		return redirect('login')


class BlogCreate(LoginRequiredMixin, UserPassesTestMixin, View):
	template_name = 'custom_admin/blog/create.html'
	login_url = reverse_lazy('login')
	form_class = BlogPostCreateForm
	context = dict()

	def test_func(self):
		return self.request.user.is_superuser

	def handle_no_permission(self):
		messages.error(self.request, 'Permission denied!!!')
		return redirect('login')

	def get(self, request):
		self.context.clear()
		self.context['ckeditor'] = True
		print(self.context)
		return render(request, self.template_name, self.context)

	def post(self, request, *args, **kwargs):
		self.context.clear()
		form = self.form_class(request.POST, request.FILES)
		self.context['form'] = form
		if form.is_valid():
			print(form.cleaned_data)
			BlogPost.objects.create(
				created_by=request.user,
				title_image=form.cleaned_data.get('title_image', ''),
				title=form.cleaned_data.get('title'),
				description=form.cleaned_data.get('bp_description'),
				slug=slugify(form.cleaned_data.get('title'))
			)
			messages.success(self.request, 'Blog has been created successfully.')
			return HttpResponseRedirect(reverse('blog-list'))
		else:
			error = Util.form_validation_error(request, form)
			self.context['error'] = error
		return render(request, self.template_name, self.context)


class BlogEdit(LoginRequiredMixin, UserPassesTestMixin, View):
	template_name = 'custom_admin/blog/edit.html'
	login_url = reverse_lazy('login')
	form_class = BlogPostEditForm
	context = dict()

	def test_func(self):
		return self.request.user.is_superuser

	def handle_no_permission(self):
		messages.error(self.request, 'Permission denied!!!')
		return redirect('login')

	def get(self, request, **kwargs):
		self.context.clear()
		self.context['ckeditor'] = True
		self.context['blog'] = BlogPost.objects.get(pk=kwargs['pk'])
		print(self.context, kwargs['pk'])
		return render(request, self.template_name, self.context)

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES, pk=self.context['blog'].id)
		self.context['form'] = form
		if form.is_valid():
			print(form.cleaned_data)
			blog = self.context['blog']
			blog.title_image = form.cleaned_data.get('title_image', '') or blog.title_image
			blog.title = form.cleaned_data.get('title')
			blog.is_verified = form.cleaned_data.get('is_verified')
			blog.description = form.cleaned_data.get('bp_description')
			blog.slug = slugify(form.cleaned_data.get('title'))
			blog.save()
			messages.success(self.request, 'Blog has been updated successfully.')
			return HttpResponseRedirect(reverse('blog-list'))
		else:
			error = Util.form_validation_error(request, form)
			self.context['error'] = error
		return render(request, self.template_name, self.context)


class BlogDelete(LoginRequiredMixin, UserPassesTestMixin, View):
	template_name = 'custom_admin/blog/list.html'
	login_url = reverse_lazy('login')

	def test_func(self):
		return self.request.user.is_superuser

	def handle_no_permission(self):
		messages.error(self.request, 'Permission denied!!!')
		return redirect('login')

	def get(self, request, **kwargs):
		BlogPost.objects.get(pk=kwargs['pk']).delete()
		messages.success(self.request, 'Blog has been deleted successfully.')
		return HttpResponseRedirect(reverse('blog-list'))


class UserList(LoginRequiredMixin, UserPassesTestMixin, ListView):
	template_name = 'custom_admin/user/list.html'
	login_url = reverse_lazy('login')
	queryset = User.objects.all()
	paginate_by = 10
	context_object_name = 'user_list'

	def test_func(self):
		return self.request.user.is_superuser

	def handle_no_permission(self):
		messages.error(self.request, 'Permission denied!!!')
		return redirect('login')


class UserEdit(LoginRequiredMixin, UserPassesTestMixin, View):
	template_name = 'custom_admin/user/edit.html'
	login_url = reverse_lazy('login')
	form_class = UserEditForm
	context = dict()

	def test_func(self):
		return self.request.user.is_superuser

	def handle_no_permission(self):
		messages.error(self.request, 'Permission denied!!!')
		return redirect('login')

	def get(self, request, **kwargs):
		self.context['user'] = User.objects.get(pk=kwargs['pk'])
		print(self.context, kwargs['pk'])
		return render(request, self.template_name, self.context)

	def post(self, request, *args, **kwargs):
		self.context['user'] = User.objects.get(pk=kwargs['pk'])
		form = self.form_class(request.POST, request.FILES, pk=self.context['user'].id)
		self.context['form'] = form
		if form.is_valid():
			print(form.cleaned_data)
			user = self.context['user']
			user.avatar = form.cleaned_data.get('avatar') or user.avatar
			user.first_name = form.cleaned_data.get('first_name', '')
			user.last_name = form.cleaned_data.get('last_name', '')
			user.phone = form.cleaned_data.get('phone', '')
			user.is_superuser = form.cleaned_data.get('is_superuser', False)
			user.is_staff = form.cleaned_data.get('is_staff', False)
			user.is_active = form.cleaned_data.get('is_active', False)
			user.save()

			messages.success(self.request, 'User has been updated successfully.')
			return HttpResponseRedirect(reverse('user-list'))
		else:
			error = Util.form_validation_error(request, form)
			self.context['error'] = error
			print('Error:', error)
		return render(request, self.template_name, self.context)

