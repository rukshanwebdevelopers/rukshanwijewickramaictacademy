from celery import shared_task
from enrollment.models import Enrollment, EnrollmentStatusType

@shared_task
def lock_monthly_enrollments():
    updated = Enrollment.objects.update(status=EnrollmentStatusType.LOCKED)
    return f"Locked {updated} enrollments"
