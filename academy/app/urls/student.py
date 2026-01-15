from django.urls import path

from academy.app.views.student.base import StudentViewSet, StudentEnrollmentsEndpoint

urlpatterns = [
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
        "students/<uuid:pk>/enrollments",
        StudentEnrollmentsEndpoint.as_view(),
        name="student-enrollments",
    ),

]
