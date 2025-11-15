from rest_framework import serializers

from authentication.models import User
from authentication.serializers import UserCreateSerializer, UserLiteSerializer
from user.models import Student, GradeLevel, AcademicYear


class AdminListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'mobile_number', 'email', 'display_name', 'first_name', 'last_name', 'is_active']


class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'mobile_number', 'email', 'display_name', 'first_name', 'last_name', 'is_active']


class StudentSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(write_only=True)

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = [
            "id",
            "created_by",
            "updated_by",
            "created_at",
            "updated_at",
            "user",
            "student_number"
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        # Create User
        user_serializer = UserCreateSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Create Student
        try:
            student = Student.objects.create(user=user, **validated_data)
            return student
        except Exception as e:
            user.delete()
            raise e


class StudentListSerializer(serializers.ModelSerializer):
    user = UserLiteSerializer()

    class Meta:
        model = Student
        fields = ['id', 'student_number', 'date_of_birth', 'gender', 'user']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'mobile_number', 'email', 'display_name', 'first_name', 'last_name', 'is_active']


class AcademicYearListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = '__all__'


class GradeLevelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeLevel
        fields = '__all__'
