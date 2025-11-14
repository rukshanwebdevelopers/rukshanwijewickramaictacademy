from core.serializers.base import BaseSerializer
from course.models import Course
from subject.serializers import SubjectListSerializer
from user.serializers import UserListSerializer


class CourseSerializer(BaseSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(BaseSerializer):
    subject = SubjectListSerializer()
    teacher = UserListSerializer()

    class Meta:
        model = Course
        fields = '__all__'
