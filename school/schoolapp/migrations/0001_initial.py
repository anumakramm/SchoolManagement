# Generated by Django 5.1.4 on 2024-12-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('course_code', models.CharField(max_length=10, unique=True)),
                ('enrollment_capacity', models.PositiveIntegerField()),
                ('semesters_offered', models.CharField(choices=[('F', 'Fall'), ('W', 'Winter'), ('S', 'Summer')], max_length=255)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('student_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('enrollment_date', models.DateField()),
                ('registered_courses', models.ManyToManyField(to='schoolapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_num', models.CharField(max_length=15)),
                ('staff_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('courses', models.ManyToManyField(limit_choices_to=2, to='schoolapp.course')),
            ],
        ),
    ]
