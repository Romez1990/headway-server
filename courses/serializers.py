from rest_framework.serializers import (
    ModelSerializer,
)

from courses.models import (
    User,
    Case,
    Course,
    CourseProgress,
)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CaseSerializer(ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseProgressSerializer(ModelSerializer):
    class Meta:
        model = CourseProgress
        fields = '__all__'
