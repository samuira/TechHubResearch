from django import forms
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from blog.models import BlogPost


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
			messages.error(self.request, 'password mis-matched')
			raise forms.ValidationError(
				_('password_mismatch'),
				code='password_mismatch',
			)
		return self.cleaned_data

#
# class BlogPostCreateForm(forms.ModelForm):
# 	class Meta:
# 		model = BlogPost
# 		fields = ['created_on', 'title_image', '']
#
# 	def __init__(self, *args, **kwargs):
# 		self.user = kwargs.pop('user')
# 		super(BlogPostCreateForm, self).__init__(*args, **kwargs)
#
# 	def clean_title(self):
# 		title = self.cleaned_data['title']
# 		if BlogPost.objects.filter(title=title).exists():
# 			messages.error(self.request, 'A blog with same title have already been written.')
# 			raise forms.ValidationError("A blog with same title have already been written.")
# 		return title

