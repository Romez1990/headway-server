from django.db.models import (
    Model,
    CharField,
    IntegerField,
    TextChoices,
    ForeignKey,
    CASCADE,
)


class User(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    age = IntegerField()
    gender = TextChoices('male', 'female')
    subdivision = CharField(max_length=100)
    status = CharField(max_length=100)


class Case(Model):
    name = CharField(max_length=255)


class Course(Model):
    name = CharField(max_length=255)


class CourseProgress(Model):
    user = ForeignKey(User, CASCADE)
    course = ForeignKey(Course, CASCADE)
    percent_complete = IntegerField()
