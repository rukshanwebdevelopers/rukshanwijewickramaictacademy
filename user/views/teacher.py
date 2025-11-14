from authentication.models import User
from core.permissions.base import ROLE
from core.views.base import BaseViewSet
from user.serializers import TeacherListSerializer


class TeacherViewSet(BaseViewSet):
    model = User
    serializer_class = TeacherListSerializer

    search_fields = ["username", "email"]

    def get_queryset(self):
        return (
            self.filter_queryset(
                super()
                .get_queryset()
                .filter(role=ROLE.TEACHER.value)
            )
        )

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
