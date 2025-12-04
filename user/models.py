from django.db import models

from authentication.models import User
from core.models.base import BaseModel


# Create your models here.
class AcademicYear(models.Model):
    """Model to track academic years (e.g., 2024-2025)"""
    name = models.CharField(max_length=20, unique=True)  # e.g., "2024-2025"
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.name


class GradeLevel(models.Model):
    """Model for grade levels (6, 7, 8, 9, 10, 11)"""
    GRADE_CHOICES = (
        (6, 'Grade 6'),
        (7, 'Grade 7'),
        (8, 'Grade 8'),
        (9, 'Grade 9'),
        (10, 'Grade 10'),
        (11, 'Grade 11'),
    )

    level = models.IntegerField(choices=GRADE_CHOICES, unique=True)
    name = models.CharField(max_length=20)  # e.g., "Sixth Grade"
    description = models.TextField(blank=True, null=True)
    next_grade = models.OneToOneField('self', on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='previous_grade')

    class Meta:
        ordering = ['level']

    def __str__(self):
        return self.name


class Student(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=20, unique=True)
    # Current academic information
    current_grade = models.ForeignKey(GradeLevel, on_delete=models.PROTECT,
                                     related_name='current_students')
    current_academic_year = models.ForeignKey(AcademicYear, on_delete=models.PROTECT,
                                            related_name='current_students')

    # Student personal information
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(
        ('male', 'Male'),
        ('female', 'Female'),
    ), blank=True, null=True)

    # Contact information
    parent_guardian_name = models.CharField(max_length=100, blank=True, null=True)
    parent_guardian_phone = models.CharField(max_length=15, blank=True, null=True)
    parent_guardian_email = models.EmailField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    emergency_contact_relation = models.CharField(max_length=50, blank=True, null=True)

    # Medical information
    medical_conditions = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    medication = models.TextField(blank=True, null=True)

    # Academic status
    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['student_number']

    def __str__(self):
        return f"{self.student_number}"

    def save(self, *args, **kwargs):
        if not self.student_number:
            # Auto-generate student number: YYGRADE0001
            current_year = self.current_academic_year.start_date.year % 100
            grade = self.current_grade.level
            last_student = Student.objects.filter(
                current_grade=self.current_grade,
                current_academic_year=self.current_academic_year
            ).order_by('-student_number').first()

            if last_student:
                last_number = int(last_student.student_number[-4:])
                new_number = last_number + 1
            else:
                new_number = 1

            self.student_number = f"{current_year}{grade:02d}{new_number:04d}"
        super().save(*args, **kwargs)


class Teacher(BaseModel):
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    hire_date = models.DateField(auto_now_add=True)
    office_location = models.CharField(max_length=50, blank=True, null=True)
    office_hours = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name}"
