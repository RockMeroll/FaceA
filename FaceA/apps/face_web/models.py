from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator


class CustomUser(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True


class Myclass(models.Model):
    myclass_id = models.IntegerField(primary_key=True, db_column='class_id')
    myclass_name = models.CharField(db_column='class_name', max_length=20)

    def __str__(self):
        return self.myclass_name

    class Meta:
        # managed = False
        db_table = 'all_class'


class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True, db_column='subject_id')
    subject_name = models.CharField(db_column='subject_name', max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    myclass = models.ForeignKey(Myclass, on_delete=models.CASCADE)

    def __str__(self):
        return '-'.join([self.subject_name, str(self.myclass)])

    class Meta:
        # managed = True
        db_table = 'all_subject'


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True, db_column='student_id')
    student_no = models.IntegerField(db_column='student_no')
    student_name = models.CharField(db_column='student_name', max_length=20)
    myclass = models.ForeignKey(Myclass, on_delete=models.CASCADE)

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


class Result(models.Model):
    result_datetime = models.DateTimeField(db_column='result_datetime')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return ''.join([str(self.student), 'is absent from', str(self.subject), 'at', str(self.datetime)])

    class Meta:
        # managed = False
        db_table = 'all_result'


