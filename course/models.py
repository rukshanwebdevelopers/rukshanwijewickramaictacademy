from django.db import models

from core.models.base import BaseModel
from subject.models import Subject
from user.models import Teacher, GradeLevel


# Create your models here.
class Course(BaseModel):
    name = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    # fee = models.FloatField()
    # batch = models.PositiveIntegerField(default=1)

    subject = models.ForeignKey(
        Subject,
        related_name="courses",
        on_delete=models.CASCADE
    )
    # teacher = models.ForeignKey(
    #     Teacher,
    #     related_name="courses",
    #     on_delete=models.CASCADE
    # )

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.name


class CourseOffering(BaseModel):
    fee = models.FloatField()
    year = models.PositiveIntegerField()
    batch = models.PositiveIntegerField()

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    grade_level = models.ForeignKey(GradeLevel, related_name="offerings", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="offerings", on_delete=models.CASCADE)

    class Meta:
        db_table = "course_offering"
        unique_together = ("course", "grade_level", "year", "batch")
