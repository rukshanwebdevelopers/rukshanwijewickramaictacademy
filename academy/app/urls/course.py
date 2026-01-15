from django.urls import path

from academy.app.views.course.base import CourseViewSet
from academy.app.views.course.offering import CourseOfferingViewSet

urlpatterns = [
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
