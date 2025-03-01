"""
Courses Database Models.
"""
from django.db import models
from users import models as user_model
from django.conf import settings

from django.db import models

class Student(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    codeGrade_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Professor(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name="user_professor")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Class(models.Model):
    name = models.CharField(max_length=50, unique=True)
    professors = models.ManyToManyField(
        Professor,
        through="ProfessorClassSection",
        help_text="Professors teaching this class"
    )

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ProfessorClassSection(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="prof_class_sections")
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    section_number = models.IntegerField(blank=True, null=True, help_text="Section number if applicable")

    class Meta:
        unique_together = ('professor', 'class_instance', 'semester', 'section_number')
        ordering = ['semester', 'class_instance']

    def __str__(self):
        return f"{self.professor} - {self.class_instance} - {self.semester} (Section {self.section_number})"


class Enrollment(models.Model):
    """
    Enrollment Model
    ----------------
    This model serves as a bridge between the Student and ProfessorClassSection models.
    It ensures that each student is uniquely associated with a class section and allows us to store
    additional metadata about the enrollment, such as the enrollment date.
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    professor_class_section = models.ForeignKey(ProfessorClassSection, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True, help_text="The date the student was enrolled")

    class Meta:
        unique_together = ('student', 'professor_class_section')
        # This ensures that each student can only be enrolled once in a given class section

    def __str__(self):
        return f"{self.student} enrolled in {self.professor_class_section}"


