from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User

def validate_gmail(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError("Enter a valid Gmail address")

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True, validators=[validate_gmail])
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.username})"

class All_course(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=30)
    c_content = models.TextField()
    syllabus = models.TextField()
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Check if the slug is not set
            self.slug = slugify(self.title)  # Generate slug from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Certification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(All_course, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    certificate_code = models.CharField(max_length=20, unique=True)
    course_start = models.DateField(null=True, blank=True)
    course_comp = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.clean()  # Call custom clean method
        super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        return f"Certification for {self.user.firstname} {self.user.lastname} - {self.course}"
