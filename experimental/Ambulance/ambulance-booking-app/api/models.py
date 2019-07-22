
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
	def create_user(self, user_email, password):
		"""
		Creates and saves a User with the given username, password.
		"""
		if not user_email:
			raise ValueError('Users must have an email')

		user = self.model(user_email=user_email)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, user_email, password):
		"""
		Creates and saves a superuser with the given username and password.
		Apply is_superuser status is TRUE
		"""
		user = self.create_user(user_email=user_email, password=password)
		user.is_superuser = True
		user.is_active = True
		user.save()
		return user


class OTP(models.Model):
	otp_type = models.CharField(max_length=50, unique=True)
	counter = models.IntegerField(default=0)
	secret_key = models.CharField(max_length=20)
	is_verified = models.SmallIntegerField(default=0)


class User(AbstractBaseUser, PermissionsMixin):
	user_email = models.EmailField(max_length=60, unique=True)
	full_name = models.CharField(max_length=60, blank=True, default='')
	user_phone = models.CharField(max_length=20, unique=True)
	is_staff = models.BooleanField(default=True)
	is_active = models.BooleanField(default=False)
	otp_secret_key = models.CharField(max_length=20, default='')
	otp_counter = models.IntegerField(default=0)
	profile_picture = models.ImageField(upload_to='profile/%Y/%m/%d', blank=True, null=True)
	country_code = models.CharField(max_length=5, default='')
	rating = models.CharField(max_length=2, default='0')
	device_type = models.CharField(max_length=20, default='')
	device_token = models.CharField(max_length=200, default='')
	is_verified = models.SmallIntegerField(default=0)

	USERNAME_FIELD = 'user_email'
	objects = UserManager()

	def __str__(self):
		return self.user_email


class AmbulanceType(models.Model):
	ambulance_type = models.CharField(max_length=20, unique=True)
	ambulance_data = models.TextField()
	base_fare = models.FloatField(default=0.0)
	ambulance_minprice = models.FloatField(default=0.0)
	ambulance_maxprice = models.FloatField(default=0.0)
	cost_per_minute = models.FloatField(default=0.0)
	cost_per_km = models.FloatField(default=0.0)
	currency = models.CharField(max_length=10)

	def __str__(self):
		return self.ambulance_type
