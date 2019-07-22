from django.urls import path
from . import views

urlpatterns = [
	path('hello/', views.HelloView.as_view(), name='HelloView'),
	path('signup/', views.SignUp.as_view(), name='SignUp'),
	path('login/', views.Login.as_view(), name='Login'),
	path('signup_otp_verification/', views.SignUpOTPVerification.as_view(), name='SignUpOTPVerification'),
	path('forget_password/', views.ForgetPassword.as_view(), name='ForgetPassword'),
	path('get_ambulance/', views.GetAmbulance.as_view(), name='GetAmbulance'),
	path('get_profile_details/', views.GetProfileDetails.as_view(), name='GetProfileDetails'),
	path('edit_profile/', views.EditProfile.as_view(), name='EditProfile'),
	path('logout/', views.Logout.as_view(), name='Logout'),
	path('get_otp_phone/', views.GetOtpPhone.as_view(), name='GetOtpPhone'),
	path('verify_otp_phone/', views.VerifyOtpPhone.as_view(), name='VerifyOtpPhone'),
]
