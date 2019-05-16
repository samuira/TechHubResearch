from django import forms
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from blog.models import BlogPost
from custom_admin.models import User


class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)
	c_password = forms.CharField(max_length=32, widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(RegisterForm, self).__init__(*args, **kwargs)

	def clean(self):
		password = self.cleaned_data.get('password')
		c_password = self.cleaned_data.get('c_password')
		if password and c_password and password != c_password:
			raise forms.ValidationError(
				_('password_mismatch'),
				code='password_mismatch',
			)
		return self.cleaned_data


class UserEditForm(forms.Form):
	avatar = forms.ImageField(required=False)
	first_name = forms.CharField(required=False, max_length=300)
	last_name = forms.CharField(required=False, max_length=300)
	phone = forms.CharField(required=False, max_length=300)
	is_superuser = forms.BooleanField(required=False)
	is_staff = forms.BooleanField(required=False)
	is_active = forms.BooleanField(required=False)

	def __init__(self, *args, **kwargs):
		self.pk = kwargs.pop('pk', None)
		super(UserEditForm, self).__init__(*args, **kwargs)

	def clean(self):
		phone = self.cleaned_data.get('phone')
		if phone and User.objects.filter(phone__iexact=phone).exclude(pk=self.pk).exists():
			raise forms.ValidationError(
				_('A user with same phone no. have already been exist.'),
				code='phone',)
		return self.cleaned_data


class BlogPostCreateForm(forms.Form):
	title_image = forms.ImageField(required=False)
	title = forms.CharField(max_length=300)
	bp_description = forms.CharField(required=True, widget=forms.Textarea)

	def clean(self):
		title = self.cleaned_data.get('title')
		if BlogPost.objects.filter(title__iexact=title).exists():
			raise forms.ValidationError(
				_('A blog with same title have already been written.'),
				code='title',)
		return self.cleaned_data


class BlogPostEditForm(BlogPostCreateForm):
	is_verified = forms.BooleanField(required=False)

	def __init__(self, *args, **kwargs):
		self.pk = kwargs.pop('pk', None)
		super(BlogPostEditForm, self).__init__(*args, **kwargs)

	def clean(self):
		title = self.cleaned_data.get('title')
		if BlogPost.objects.filter(title__iexact=title).exclude(pk=self.pk).exists():
			raise forms.ValidationError(
				_('A blog with same title have already been written.'),
				code='title',)
		return self.cleaned_data