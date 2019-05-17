from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.excempt_csrf import CsrfExemptSessionAuthentication
from blog.models import BlogPost
from blog.serializers import BlogListSerializer


class BlogList(APIView):
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	permission_classes = (AllowAny,)
	authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

	def post(self, request, format=None):
		print(request.POST)
		query_set = BlogPost.objects.filter(is_verified=True)
		serializer = BlogListSerializer(query_set, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


