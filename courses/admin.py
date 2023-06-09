from django.contrib import admin

from .models import Category, Instructor, Course, Enrollment, Chapter, FrequentlyAskedQuestion, CustomerMessage

admin.site.register(Instructor)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Enrollment)
admin.site.register(FrequentlyAskedQuestion)
admin.site.register(CustomerMessage)