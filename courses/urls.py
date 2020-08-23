from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    UserViewSet,
    CaseViewSet,
    CourseViewSet,
    CourseProgressViewSet,
)

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('cases', CaseViewSet, basename='cases')
router.register('courses', CourseViewSet, basename='courses')
router.register('course-progresses', CourseProgressViewSet, basename='course-progresses')

urlpatterns = [
    path('', include(router.urls)),
]
