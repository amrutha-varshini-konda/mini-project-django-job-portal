from django.contrib import admin
from django.urls import path
from core.views import JobListCreateView, ApplicationCreateView, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/jobs/', JobListCreateView.as_view(), name='job-list-create'),
    path('api/applications/', ApplicationCreateView.as_view(), name='application-list-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]