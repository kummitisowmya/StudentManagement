from django.contrib import admin
from students.models import *
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Material)
admin.site.register(StudentCourse)