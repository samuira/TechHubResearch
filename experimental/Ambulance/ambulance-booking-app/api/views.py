from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .excempt_csrf import CsrfExemptSessionAuthentication
from .models import User, AmbulanceType
from .utils import Utils
from .serializers import UserSerializer, LoginSerializer, OTPVerificationSerializer, ForgetPasswordSerializer, \
	GetAmbulanceSerializer, AmbulanceTypeSerializer, EditProfileSerializer, GetOtpPhoneSerializer, \
	VerifyOtpPhoneSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, BasicAuthentication


class HelloView(APIView):
	def get(self, request):
		content = {'message': 'Hello, World!'}
		return Response(content)


class SignUp(APIView):
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	permission_classes = (AllowAny,)
	authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		data = request.data.copy()
		print('data:', type(data))
		if serializer.is_valid():

			otp_secret_key = Utils.generate_secret_key_hotp()
			data['otp_secret_key'] = otp_secret_key
			ph_with_con_id = Utils.find_numbers_re(data['user_phone'])
			if len(ph_with_con_id) == 2:
				data['country_code'] = ph_with_con_id[0]
				data['user_phone'] = ph_with_con_id[1]
				phone_no = '+{}'.format(''.join(ph_with_con_id))
				print('phone_no:', phone_no)
				print(User.objects.filter(user_email=data['user_email']),
					  User.objects.filter(user_phone=data['user_phone']))
				print(User.objects.filter(user_email=data['user_email']) or User.objects.filter(
					user_phone=data['user_phone']))
				if User.objects.filter(user_email=data['user_email']):
					res = {
						"status": False,
						"message": "email already exist.",
						"error": {
							"user_email": "email already exist."
						}
					}
					return Response(res, status=status.HTTP_200_OK)
				elif User.objects.filter(user_phone=data['user_phone']):
					res = {
						"status": False,
						"message": "phone number already exist.",
						"error": {
							"user_phone": "phone number already exist."
						}
					}
					return Response(res, status=status.HTTP_200_OK)

				else:
					res = {
						"status": True,
						"message": "Successfully signed up.OTP generated and sent to registered phone number.",
						"otp": Utils.generate_hotp(0, otp_secret_key),
						"error": None
					}
					serializer.create(data)
					return Response(res, status=status.HTTP_200_OK)

			else:
				res = {
					"status": False,
					"message": "Please provide the user_phone with country code using a separator like this : XX-XXXXXXXXXX",
					"error": {
						"user_phone": "Please provide the user_phone with country code using a separator like this : XX-XXXXXXXXXX"
					}
				}
				return Response(res, status=status.HTTP_200_OK)
		################################################################################################################
		# TODO: setup twilio account and uncomment the code
		# sms = 'Your ambulance booking app account varification otp is {}'.format(otp)
		# stat, msg = Utils.send_sms(sms, phone_no)
		# print('status:', status)
		# if stat == 200:
		# 	res = {
		# 		"status": True,
		# 		"message": "Successfully signed up.OTP generated and sent to registered phone number.",
		# 	}
		# 	serializer.create(data)
		# else:
		# 	print(msg)
		# 	res = {
		# 		"status": False,
		# 		"message": msg,
		# 	}
		################################################################################################################
		error = {}
		msg = ''
		for k, v in serializer.errors.items():
			error[k] = v[0]
			msg = msg + k + " -> " + v[0] + ' '
		res = {
			"status": False,
			"message": msg,
			"error": error
		}
		return Response(res, status=status.HTTP_200_OK)


class Login(APIView):
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	permission_classes = (AllowAny,)
	authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

	def post(self, request, format=None):
		data = request.data.copy()
		print(data)
		user_id = data.get('user_id', '')
		print(user_id)
		if not user_id.strip():
			res = {
				"status": False,
				"message": "Please provide email or phone to login.",
				"error": {
					"user_id": "Please provide email or phone to login."
				}
			}
			return Response(res, status=status.HTTP_200_OK)
		elif '@' in user_id:
			data['user_email'] = user_id
		else:
			data['user_phone'] = user_id
		serializer = LoginSerializer(data=data)
		if serializer.is_valid():
			user_email = serializer.validated_data.get('user_email', None)
			password = serializer.validated_data.get('password', None)

			if not user_email:
				user_phone = serializer.validated_data.get('user_phone', None)
				if not user_phone:
					res = {
						"status": False,
						"message": "Please provide user_email or user_phone to login.",
						"error": {
							"user_id": "Please provide user_email or user_phone to login."
						}
					}
					return Response(res, status=status.HTTP_200_OK)
				else:
					ph_with_con_id = Utils.find_numbers_re(user_phone)
					if len(ph_with_con_id) == 1:
						user_phone = ph_with_con_id[0]
					elif len(ph_with_con_id) == 2:
						user_phone = ph_with_con_id[1]
					else:
						res = {
							"status": False,
							"message": "Please provide phone no with format like this: XXXXXXXXXX (without country "
									   "code) or XX-XXXXXXXXXX (with country code)",
							"error": {
								"user_id": "Please provide phone no with format like this: XXXXXXXXXX (without country "
										   "code) or XX-XXXXXXXXXX (with country code) "
							}
						}
						return Response(res, status=status.HTTP_200_OK)
					try:
						user_email = User.objects.get(user_phone=user_phone).user_email
					except Exception as e:
						res = {
							"status": False,
							"message": "user id is not found.",
							"error": {
								"user_id": "user id is not found."
							}
						}
						return Response(res, status=status.HTTP_200_OK)
			print(user_email, password)
			if user_email:
				try:
					user_obj = User.objects.get(user_email=user_email)
					if not user_obj.is_active:
						res = {
							"status": False,
							"message": "Account has not been activated. Please activate your account.",
							"error": {
								"user_id": "Account has not been activated. Please activate your account."
							}
						}
						return Response(res, status=status.HTTP_200_OK)
				except User.DoesNotExist as e:
					res = {
						"status": False,
						"message": "user id is not found.",
						"error": {
							"user_id": "user id is not found."
						}
					}
					return Response(res, status=status.HTTP_200_OK)
				else:
					user = authenticate(request=request, user_email=user_email, password=password)
					if not user:
						res = {
							"status": False,
							"message": "Wrong password provided.",
							"error": {
								"password": "Wrong password provided."
							}
						}
						return Response(res, status=status.HTTP_200_OK)
					else:
						token_key, token = Token.objects.get_or_create(user=user)
						login(request, user)
						res = {
							"status": True,
							"message": "Successfully logged in.",
							"data": {
								"access_token": token_key.key,
								"full_name": user.full_name,
								"profile_picture": str(user.profile_picture) if user.profile_picture else '',
								"user_email": user.user_email,
								"user_phone": user.user_phone,
								"country_code": user.country_code,
								"rating": int(user.rating),
								"is_verified": user.is_verified
							},
							"error": None
						}
						return Response(res, status=status.HTTP_200_OK)

			else:
				res = {
					"status": False,
					"message": "user id is not found.",
					"error": {
						"user_id": "user id is not found."
					}
				}
				return Response(res, status=status.HTTP_200_OK)
		error = {}
		msg = ''
		for k, v in serializer.errors.items():
			error[k] = v[0]
			msg = msg + k + " -> " + v[0] + ' '
		res = {
			"status": False,
			"message": msg,
			"error": error
		}
		return Response(res, status=status.HTTP_200_OK)


class SignUpOTPVerification(APIView):
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	permission_classes = (AllowAny,)
	authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

	def post(self, request, format=None):
		serializer = OTPVerificationSerializer(data=request.data)
		if serializer.is_valid():
			user_email = serializer.validated_data['user_email']
			user_phone = serializer.validated_data['user_phone']
			ph_with_con_id = Utils.find_numbers_re(user_phone)
			if len(ph_with_con_id) == 1:
				user_phone = ph_with_con_id[0]
			elif len(ph_with_con_id) == 2:
				user_phone = ph_with_con_id[1]
			else:
				res = {
					"status": False,
					"message": "Please provide phone no with format like this: XXXXXXXXXX (without country code)"
							   " or XX-XXXXXXXXXX (with country code)",
					"error": {
						"user_phone": "Please provide phone no with format like this: XXXXXXXXXX (without country code)"
									  " or XX-XXXXXXXXXX (with country code)"
					}
				}
				return Response(res, status=status.HTTP_200_OK)

			try:
				user = User.objects.get(user_email=user_email)
			except User.DoesNotExist as e:
				print(e)
				res = {
					"status": False,
					"message": "Wrong email address provided.",
					"error": {
						"user_email": "Wrong email address provided."
					}
				}
				return Response(res, status=status.HTTP_200_OK)
			else:
				if user.is_active:
					res = {
						"status": False,
						"message": "Account is already activated.",
						"error": {
							"user_email": "Account is already activated."
						}
					}
					return Response(res, status=status.HTTP_200_OK)
				elif user.user_phone != user_phone:
					res = {
						"status": False,
						"message": "Wrong phone number provided.",
						"error": {
							"user_phone": "Wrong phone number provided."
						}
					}
					return Response(res, status=status.HTTP_200_OK)
				else:
					if Utils.verify_hotp(serializer.validated_data['otp'], user.otp_counter, user.otp_secret_key):
						token_key, token = Token.objects.get_or_create(user=user)
						res = {
							"status": True,
							"message": "Successfully verified.",
							"data": {
								"access_token": token_key.key,
								"full_name": user.full_name,
								"profile_picture": str(user.profile_picture) if user.profile_picture else '',
								"user_email": user.user_email,
								"user_phone": user.user_phone,
								"country_code": user.country_code,
								"rating": int(user.rating),
								"is_verified": user.is_verified
							},
							"error": None
						}
						serializer.update(user, serializer.validated_data)
						return Response(res, status=status.HTTP_200_OK)
					else:
						res = {
							"status": False,
							"message": "Wrong OTP provided.",
							"error": {
								"otp": "Wrong OTP provided."
							}
						}
						return Response(res, status=status.HTTP_200_OK)
		error = {}
		msg = ''
		for k, v in serializer.errors.items():
			error[k] = v[0]
			msg = msg + k + " -> " + v[0] + ' '
		res = {
			"status": False,
			"message": msg,
			"error": error
		}
		return Response(res, status=status.HTTP_200_OK)


class ForgetPassword(APIView):
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	permission_classes = (AllowAny,)
	authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

	def post(self, request, format=None):
		serializer = ForgetPasswordSerializer(data=request.data)
		if serializer.is_valid():
			user_email = serializer.validated_data.get('user_email', None)
			user_phone = serializer.validated_data.get('user_phone', None)
			if user_phone or user_email:
				if not user_email:
					ph_with_con_id = Utils.find_numbers_re(user_phone)
					if len(ph_with_con_id) == 1:
						user_phone = ph_with_con_id[0]
					elif len(ph_with_con_id) == 2:
						user_phone = ph_with_con_id[1]
					else:
						res = {
							"status": False,
							"message": "Please provide phone no with format like this: XXXXXXXXXX (without country code)"
									   " or XX-XXXXXXXXXX (with country code)",
							"error": {
								"user_phone": "Please provide phone no with format like this: XXXXXXXXXX (without "
											  "country code) or XX-XXXXXXXXXX (with country code) "
							}
						}
						return Response(res, status=status.HTTP_200_OK)
					try:
						user_email = User.objects.get(user_phone=user_phone).user_email
					except Exception as e:
						res = {
							"status": False,
							"message": "phone no not found.",
							"error": {
								"user_phone": "phone no not found."
							}
						}
						return Response(res, status=status.HTTP_200_OK)
				try:
					User.objects.get(user_email=user_email)
				except User.DoesNotExist as e:
					res = {
						"status": False,
						"message": "Email address not found.",
						"error": {
							"user_email": "Email address not found."
						}
					}
					return Response(res, status=status.HTTP_200_OK)
				else:
					####################################################################################################
					# TODO: Reset password and send it through email.
					####################################################################################################
					res = {
						"status": True,
						"message": "Successfully sent mail to registered email id.Check mail.",
						"error": None
					}
					return Response(res, status=status.HTTP_200_OK)
			else:
				res = {
					"status": False,
					"message": "Please provide email address or phone no.",
					"error": {
						"user_email": "Please provide email address or phone no."
					}
				}
				return Response(res, status=status.HTTP_200_OK)
		error = {}
		msg = ''
		for k, v in serializer.errors.items():
			error[k] = v[0]
			msg = msg + k + " -> " + v[0] + ' '

		res = {
			"status": False,
			"message": msg,
			"error": error
		}
		return Response(res, status=status.HTTP_200_OK)


class GetAmbulance(APIView):
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	permission_classes = (IsAuthenticated,)
	authentication_classes = (TokenAuthentication,)

	def post(self, request, format=None):
		get_ambulance_serializer = GetAmbulanceSerializer(data=request.data)
		if get_ambulance_serializer.is_valid():
			print(get_ambulance_serializer.validated_data)
			ambulance_type = get_ambulance_serializer.validated_data.get('ambulance_type', 'all')
			print('ambulance_type:', ambulance_type == 'all')
			if ambulance_type == 'all':
				qs = AmbulanceType.objects.all()
			else:
				try:
					qs = [AmbulanceType.objects.get(ambulance_type=ambulance_type)]
				except AmbulanceType.DoesNotExist:
					res = {
						"status": False,
						"message": "Ambulance Type not found.",
						"error": {
							"ambulance_type": "Ambulance Type not found."
						}
					}
					return Response(res, status=status.HTTP_200_OK)

			ambulance_type_serializer = AmbulanceTypeSerializer(qs, many=True)
			res = {
				"status": True,
				"message": "Successfully got the price details.",
				"data": {
					"arr_ambulance": ambulance_type_serializer.data
				},
				"error": None
			}
			return Response(res, status=status.HTTP_200_OK)
		error = {}
		msg = ''
		for k, v in get_ambulance_serializer.errors.items():
			error[k] = v[0]
			msg = msg + k + " -> " + v[0] + ' '
		res = {
			"status": False,
			"message": msg,
			"error": error
		}
		return Response(res, status=status.HTTP_200_OK)


class GetProfileDetails(APIView):
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	permission_classes = (IsAuthenticated,)
	authentication_classes = (TokenAuthentication,)

	def post(self, request, format=None):
		if request.user.is_authenticated:
			res = {
				"status": True,
				"message": "Successfully fetched.",
				"data": {
					"full_name": request.user.full_name,
					"profile_picture": str(request.user.full_name) if request.user.full_name else "",
					"user_email": request.user.user_email,
					"user_phone": request.user.user_phone,
					"country_code": request.user.country_code,
					"rating": request.user.rating,
					"is_verified": request.user.is_verified
				},
				"error": None
			}
			return Response(res, status=status.HTTP_200_OK)
		res = {
			"status": False,
			"message": "User is not authenticated",
			"error": {
				"user_email": "User is not authenticated"
			}
		}
		return Response(res, status=status.HTTP_200_OK)


class EditProfile(APIView):
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	permission_classes = (IsAuthenticated,)
	authentication_classes = (TokenAuthentication,)

	def post(self, request, format=None):
		data = request.data.copy()
		if request.user.user_phone == request.data.get('user_phone', request.user.user_phone):
			data.pop('user_phone', None)
		serializer = EditProfileSerializer(data=data)
		if serializer.is_valid() and request.user.is_authenticated:
			user = serializer.update(request.user, serializer.validated_data)

			res = {
				"status": True,
				"message": "Successfully fetched.",
				"data": {
					"full_name": user.full_name,
					"profile_picture": str(user.profile_picture) if user.profile_picture else "",
					"user_email": user.user_email,
					"user_phone": user.user_phone,
					"country_code": user.country_code,
					"rating": user.rating,
					"is_verified": user.is_verified
				},
				"error": None
			}
			return Response(res, status=status.HTTP_200_OK)
		error = {}
		msg = ''
		for k, v in serializer.errors.items():
			error[k] = v[0]
			msg = msg + k + " -> " + v[0] + ' '
		res = {
			"status": False,
			"message": msg,
			"error": error
		}
		return Response(res, status=status.HTTP_200_OK)


class Logout(APIView):
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	permission_classes = (IsAuthenticated,)
	authentication_classes = (TokenAuthentication,)

	def post(self, request, format=None):
		if request.user.is_authenticated:
			logout(request)
			res = {
				"status": True,
				"message": "Successfully Logged out.",
				"error":None
			}
			return Response(res, status=status.HTTP_200_OK)
		res = {
			"status": False,
			"message": "User is not authenticated",
			"error":{
				"user_email": "User is not authenticated"
			}
		}
		return Response(res, status=status.HTTP_200_OK)


class GetOtpPhone(APIView):
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	permission_classes = (IsAuthenticated,)
	authentication_classes = (TokenAuthentication,)

	def post(self, request, format=None):
		serializer = GetOtpPhoneSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.update(request.user, serializer.validated_data)
			res = {
				"status": True,
				"message": "OTP sent successfully.",
				"otp": Utils.generate_hotp(user.otp_counter, user.otp_secret_key),
				"error": None
			}
			return Response(res, status=status.HTTP_200_OK)
		error = {}
		msg = ''
		for k, v in serializer.errors.items():
			error[k] = v[0]
			msg = msg + k + " -> " + v[0] + ' '
		res = {
			"status": False,
			"message": msg,
			"error": error
		}
		return Response(res, status=status.HTTP_200_OK)


class VerifyOtpPhone(APIView):
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	permission_classes = (IsAuthenticated,)
	authentication_classes = (TokenAuthentication,)

	def post(self, request, format=None):
		serializer = VerifyOtpPhoneSerializer(data=request.data)
		if serializer.is_valid():
			if request.user.is_verified:
				res = {
					"status": False,
					"message": "Phone no already verified.",
					"error": {
						"user_email": "Phone no already verified."
					}
				}
				return Response(res, status=status.HTTP_200_OK)
			else:
				if Utils.verify_hotp(serializer.validated_data['otp'], request.user.otp_counter,
									 request.user.otp_secret_key):
					user = serializer.update(request.user, serializer.validated_data)
					res = {
						"status": True,
						"message": "OTP verified successfully.",
						"data": {
							"full_name": user.full_name,
							"profile_picture": str(user.profile_picture) if user.profile_picture else '',
							"user_email": user.user_email,
							"user_phone": user.user_phone,
							"country_code": user.country_code,
							"rating": user.rating,
							"is_verified": user.is_verified
						},
						"error": None
					}
					return Response(res, status=status.HTTP_200_OK)
				else:
					res = {
						"status": False,
						"message": "Wrong OTP provided.",
						"error": {
							"otp": "Wrong OTP provided."
						}
					}
					return Response(res, status=status.HTTP_200_OK)
		error = {}
		msg = ''
		for k, v in serializer.errors.items():
			error[k] = v[0]
			msg = msg + k + " -> " + v[0] + ' '
		res = {
			"status": False,
			"message": msg,
			"error": error
		}
		return Response(res, status=status.HTTP_200_OK)
