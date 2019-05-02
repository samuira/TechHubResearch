from django.urls import path
from .views import (Dashboard, Login, Register, BlogList, BlogEdit, BlogDelete, BlogCreate, UserList, UserEdit)

urlpatterns = [
	path('', Dashboard.as_view(), name='dashboard'),
	path('login', Login.as_view(), name='login'),
	path('register', Register.as_view(), name='register'),
	path('blog_list', BlogList.as_view(), name='blog-list'),
	path('blog_edit', BlogEdit.as_view(), name='blog-edit'),
	path('blog_create', BlogCreate.as_view(), name='blog-create'),
	path('blog_delete', BlogDelete.as_view(), name='blog-delete'),
	path('user_list', UserList.as_view(), name='user-list'),
	path('user_edit', UserEdit.as_view(), name='user-edit'),
]