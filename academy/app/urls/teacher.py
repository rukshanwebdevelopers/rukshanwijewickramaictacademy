from django.urls import path

from academy.app.views.teacher.base import TeacherViewSet

urlpatterns = [
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
]
