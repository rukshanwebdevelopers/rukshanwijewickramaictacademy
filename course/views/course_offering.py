# Create your views here.
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from core.views.base import BaseViewSet
from course.models import CourseOffering
from course.serializers import CourseOfferingListSerializer, CourseOfferingSerializer


class CourseOfferingViewSet(BaseViewSet):
    model = CourseOffering
    serializer_class = CourseOfferingListSerializer

    search_fields = ["year", "grade_level__name"]
    filterset_fields = []

    def get_queryset(self):
        return (
            self.filter_queryset(super().get_queryset())
        )

    def create(self, request, *args, **kwargs):
        try:
            course_offering = CourseOffering.objects.filter(
                course=request.data.get("course"),
                grade_level=request.data.get("grade_level"),
                year=request.data.get("year"),
                batch=request.data.get("batch"),
            ).first()

            if course_offering:
                return Response(
                    {"batch": "Course Offering already exists."},
                    status=status.HTTP_409_CONFLICT,
                )
            serializer = CourseOfferingSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data = serializer.data
                return Response(data, status=status.HTTP_201_CREATED)
            return Response(
                [serializer.errors[error][0] for error in serializer.errors],
                status=status.HTTP_400_BAD_REQUEST,
            )
        except IntegrityError as e:
            if "already exists" in str(e):
                return Response(
                    {"slug": "CourseOffering already exists."},
                    status=status.HTTP_409_CONFLICT,
                )

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
