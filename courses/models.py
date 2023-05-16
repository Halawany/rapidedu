from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):

    name = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(kwargs={"pk": self.pk})

class Instructor(models.Model):

    name = models.CharField(max_length=250)
    email = models.EmailField()
    age = models.IntegerField()
    job = models.CharField(max_length=600)

    def __str__(self):
        return f"instructor {self.name} and works as {self.job}"

class Course(models.Model):

    name = models.CharField(max_length=1000, blank=False, null=False)
    date_posted = models.DateTimeField(auto_now=True)
    instructors = models.ManyToManyField(Instructor)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=600, unique=True, blank=True)
    cover = models.ImageField(upload_to="images/cover/")

    class Meta:
        verbose_name = ("course")
        verbose_name_plural = ("courses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Enrollment(models.Model):

    ENROLLMENT_STATUS_CHOICES = [
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ENROLLMENT_STATUS_CHOICES, default='enrolled')

    class Meta:
        verbose_name = ("enroll")

    def __str__(self):
        return f"{self.user} enrolled in course {self.course}"


class Chapter(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=600, blank=False, null=False)
    description = models.TextField()
    video = models.FileField(upload_to="video/chapters/", blank=False, null=False)

    class Meta:
        verbose_name = ("chapter")
        verbose_name_plural = ("chapters")

    def __str__(self):
        return f"{self.name} from course {self.course}" 

    def get_absolute_url(self):
        return reverse(kwargs={"pk": self.pk})

class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=600)
    answer = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class CustomerMessage(models.Model):
    name = models.CharField(max_length=600)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.message} by {self.name} on {self.created_at}"