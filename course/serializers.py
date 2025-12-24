from core.serializers.base import BaseSerializer
from course.models import Course, CourseOffering
from subject.serializers import SubjectListSerializer
from user.serializers import TeacherListSerializer, GradeLevelListSerializer


class CourseSerializer(BaseSerializer):
    subject = SubjectListSerializer()
    teacher = TeacherListSerializer()

    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(BaseSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "code",
            "slug",
            "subject",
        )


class CourseOfferingSerializer(BaseSerializer):
    class Meta:
        model = CourseOffering
        fields = '__all__'


class CourseOfferingListSerializer(BaseSerializer):
    course = CourseListSerializer()
    teacher = TeacherListSerializer()
    grade_level = GradeLevelListSerializer()

    class Meta:
        model = CourseOffering
        fields = [
            'id',
            'course',
            'teacher',
            'fee',
            'year',
            'batch',
            'grade_level'
        ]
