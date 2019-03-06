# Generated by Django 2.1.7 on 2019-02-25 09:01

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myclass',
            fields=[
                ('myclass_id', models.IntegerField(db_column='class_id', primary_key=True, serialize=False)),
                ('myclass_name', models.CharField(db_column='class_name', max_length=20)),
            ],
            options={
                'db_table': 'all_class',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_datetime', models.DateTimeField(db_column='result_datetime')),
            ],
            options={
                'db_table': 'all_result',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(db_column='student_id', primary_key=True, serialize=False)),
                ('student_no', models.IntegerField(db_column='student_no')),
                ('student_name', models.CharField(db_column='student_name', max_length=20)),
                ('myclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_web.Myclass')),
            ],
            options={
                'db_table': 'all_student',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.IntegerField(db_column='subject_id', primary_key=True, serialize=False)),
                ('subject_name', models.CharField(db_column='subject_name', max_length=20)),
                ('myclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_web.Myclass')),
            ],
            options={
                'db_table': 'all_subject',
            },
        ),
        migrations.CreateModel(
            name='SubjectElective',
            fields=[
                ('subject_elective_id', models.IntegerField(db_column='subject_elective_id', primary_key=True, serialize=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_web.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_web.Subject')),
            ],
            options={
                'db_table': 'all_subject_elective',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_web.Student'),
        ),
        migrations.AddField(
            model_name='result',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_web.Subject'),
        ),
    ]