from django.urls import path
from rest_framework.routers import DefaultRouter

from user.views.academic_year import AcademicYearViewSet
from user.views.admin import AdminViewSet
from user.views.grade_level import GradeLevelViewSet
from user.views.student import StudentViewSet, StudentEnrolledCoursesEndpoint
from user.views.teacher import TeacherViewSet
from user.views.user import UserViewSet

router = DefaultRouter()

urlpatterns = [
    path(
        "admin/list/",
        AdminViewSet.as_view({"get": "list"}),
        name="admin",
    ),
    path(
        "teachers/",
        TeacherViewSet.as_view({"get": "list", "post": "create"}),
        name="teacher",
    ),
    path(
        "teachers/<uuid:pk>/",
        TeacherViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="teacher",
    ),
    path(
        "students/",
        StudentViewSet.as_view({"get": "list", "post": "create"}),
        name="student",
    ),
    path(
        "students/<uuid:pk>/",
        StudentViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="student",
    ),
    path(
        "students/<uuid:pk>/enrolled-courses/",
        StudentEnrolledCoursesEndpoint.as_view(),
        name="student-enrolled-courses",
    ),
    path(
        "users/",
        UserViewSet.as_view({"get": "list", "post": "create"}),
        name="user",
    ),
    path(
        "users/<uuid:pk>/",
        UserViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="user",
    ),
    path(
        "users/block-user",
        UserViewSet.as_view({"get": "list", "post": "create"}),
        name="user",
    ),
    path(
        "academicYears/",
        AcademicYearViewSet.as_view({"get": "list", "post": "create"}),
        name="academicYear",
    ),
    path(
        "academicYears/<uuid:pk>/",
        AcademicYearViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="academicYear",
    ),
    path(
        "gradeLevel/",
        GradeLevelViewSet.as_view({"get": "list", "post": "create"}),
        name="gradeLevel",
    ),
    path(
        "gradeLevel/<uuid:pk>/",
        GradeLevelViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="gradeLevel",
    ),
]
