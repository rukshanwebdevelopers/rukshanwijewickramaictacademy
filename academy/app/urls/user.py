from django.urls import path

from academy.app.views.user.base import UserViewSet

urlpatterns = [
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
        UserViewSet.as_view({"post": "deactivate"}),
        name="user",
    ),
]
