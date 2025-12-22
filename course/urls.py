from django.urls import include, path
from rest_framework.routers import DefaultRouter

from course.views.course import CourseViewSet
from course.views.course_offering import CourseOfferingViewSet

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(
        "courses/",
        CourseViewSet.as_view({"get": "list", "post": "create"}),
        name="course",
    ),
    path(
        "courses/<str:slug>/",
        CourseViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="course",
    ),
    path(
        "course-offerings/",
        CourseOfferingViewSet.as_view({"get": "list", "post": "create"}),
        name="course-offering",
    ),
    path(
        "course-offerings/<str:slug>/",
        CourseOfferingViewSet.as_view({
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }),
        name="course-offering",
    ),
]
