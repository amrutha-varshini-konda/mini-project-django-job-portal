from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, JobPostingViewSet, ApplicationViewSet, RegisterView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'jobs', JobPostingViewSet, basename='job')
router.register(r'jobpostings', JobPostingViewSet, basename='jobposting')  # Added this line
router.register(r'applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]