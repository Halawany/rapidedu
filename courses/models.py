from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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
    cover = models.ImageField(upload_to="images/cover/")

    class Meta:
        verbose_name = ("course")
        verbose_name_plural = ("courses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(kwargs={"pk": self.pk})

class Enrollment(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("enroll")

    def __str__(self):
        return self.name


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
