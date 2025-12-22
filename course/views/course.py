from rest_framework import status
from rest_framework.response import Response

from core.permissions.base import allow_permission, ROLE
from core.views.base import BaseViewSet
from course.models import Course
from course.serializers import CourseListSerializer, CourseSerializer


# Create your views here.
class CourseViewSet(BaseViewSet):
    model = Course
    serializer_class = CourseListSerializer

    search_fields = ["name", "slug"]
    filterset_fields = []

    lookup_field = "slug"

    def get_queryset(self):
        return (
            self.filter_queryset(super().get_queryset())
        )

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        course = self.get_queryset().filter(slug=slug).first()

        if not course:
            return Response({"detail": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @allow_permission([ROLE.ADMIN])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @allow_permission([ROLE.ADMIN])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @allow_permission([ROLE.ADMIN])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @allow_permission([ROLE.ADMIN])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
