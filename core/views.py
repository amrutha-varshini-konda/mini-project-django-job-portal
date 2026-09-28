from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by('-id')
    serializer_class = JobSerializer
    permission_classes = [AllowAny]

class ApplicationCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]