from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator


class CustomUser(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True


class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True, db_column='subject_id')
    subject_name = models.CharField(db_column='subject_name', max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name

    class Meta:
        # managed = True
        db_table = 'all_subject'


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True, db_column='student_id')
    student_no = models.IntegerField(db_column='student_no')
    student_name = models.CharField(db_column='student_name', max_length=20)

    def __str__(self):
        return self.student_name

    class Meta:
        # managed = False
        db_table = 'all_student'


class SubjectElective(models.Model):
    subject_elective_id = models.IntegerField(primary_key=True, db_column='subject_elective_id')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        # managed = False
        db_table = 'all_subject_elective'


