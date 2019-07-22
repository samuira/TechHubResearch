from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, AmbulanceType
from .utils import Utils


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('user_email', 'full_name', 'user_phone', 'password',)

	def create(self, validated_data):
		""" Creates and returns a new user """
		# Validating Data
		user = User(
			full_name=validated_data['full_name'] if validated_data.get('full_name', None) else '',
			user_email=validated_data['user_email'],
			user_phone=validated_data['user_phone'],
			otp_secret_key=validated_data['otp_secret_key'],
			country_code=validated_data['country_code']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user


class LoginSerializer(serializers.Serializer):
	password = serializers.CharField(max_length=100, required=True)
	user_email = serializers.EmailField(max_length=60, required=False)
	user_phone = serializers.CharField(max_length=20, required=False)
	device_type = serializers.CharField(max_length=20,required=True)
	device_token = serializers.CharField(max_length=200, required=False)

	def update(self, instance, validated_data):
		pass

	def create(self, validated_data):
		pass


class OTPVerificationSerializer(serializers.Serializer):
	otp = serializers.CharField(max_length=4, required=True)
	user_phone = serializers.CharField(max_length=20, required=True)
	user_email = serializers.EmailField(max_length=60, required=True)
	device_type = serializers.CharField(max_length=20,required=True)
	device_token = serializers.CharField(max_length=200, required=False)

	def update(self, instance, validated_data):
		instance.is_active = True
		instance.is_verified = 1
		instance.otp_counter = instance.otp_counter + 1
		instance.save()
		return instance

	def create(self, validated_data):
		pass


class ForgetPasswordSerializer(serializers.Serializer):
	user_phone = serializers.CharField(max_length=20, required=False)
	user_email = serializers.EmailField(max_length=60, required=False)

	def update(self, instance, validated_data):
		pass

	def create(self, validated_data):
		pass


class GetAmbulanceSerializer(serializers.Serializer):
	lat_pick_up = serializers.CharField(max_length=30, required=True)
	lng_pick_up = serializers.CharField(max_length=30, required=True)
	lat_destination = serializers.CharField(max_length=30, required=True)
	lng_destination = serializers.CharField(max_length=30, required=True)
	ambulance_type = serializers.CharField(max_length=30, required=False)
	schedule_time = serializers.CharField(max_length=30, required=True)

	def update(self, instance, validated_data):
		pass

	def create(self, validated_data):
		pass


class AmbulanceTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = AmbulanceType
		fields = ('ambulance_type', 'ambulance_data', 'ambulance_minprice', 'ambulance_maxprice', 'currency',)


class EditProfileSerializer(serializers.Serializer):
	full_name = serializers.CharField(max_length=60, required=False)
	profile_picture = serializers.ImageField(required=False)
	user_phone = serializers.CharField(max_length=20, required=False, validators=[UniqueValidator(queryset=User.objects.all())])
	country_code = serializers.CharField(max_length=5, required=False)

	def update(self, instance, validated_data):
		print('instance:', instance)
		print('validated_data:', validated_data)
		instance.full_name = validated_data.get('full_name', instance.full_name)
		instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
		if instance.user_phone is not validated_data.get('user_phone', instance.user_phone):
			instance.user_phone = validated_data.get('user_phone', instance.user_phone)
		instance.country_code = validated_data.get('country_code', instance.country_code)
		instance.save()
		return instance

	def create(self, validated_data):
		pass


class GetOtpPhoneSerializer(serializers.Serializer):
	user_phone = serializers.CharField(max_length=20, required=True, validators=[UniqueValidator(queryset=User.objects.all())])
	country_code = serializers.CharField(max_length=5, required=True)

	def update(self, instance, validated_data):
		instance.otp_counter = instance.otp_counter + 1
		instance.user_phone = validated_data['user_phone']
		instance.country_code = validated_data['country_code']
		instance.is_verified = 0
		instance.save()
		return instance

	def create(self, validated_data):
		pass


class VerifyOtpPhoneSerializer(serializers.Serializer):
	user_phone = serializers.CharField(max_length=20, required=True, validators=[UniqueValidator(queryset=User.objects.all())])
	country_code = serializers.CharField(max_length=5, required=True)
	otp = serializers.CharField(max_length=4, required=True)

	def update(self, instance, validated_data):
		instance.otp_counter = instance.otp_counter + 1
		instance.is_verified = 1
		instance.save()
		return instance

	def create(self, validated_data):
		pass


