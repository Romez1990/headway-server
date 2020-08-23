from rest_framework.viewsets import ModelViewSet

from .serializers import (
    UserSerializer,
    CaseSerializer,
    CourseSerializer,
    CourseProgressSerializer,
)
from .models import (
    User,
    Case,
    Course,
    CourseProgress,
)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects


class CaseViewSet(ModelViewSet):
    serializer_class = CaseSerializer
    queryset = Case.objects


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects


class CourseProgressViewSet(ModelViewSet):
    serializer_class = CourseProgressSerializer
    queryset = CourseProgress.objects
