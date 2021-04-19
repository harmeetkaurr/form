from django.contrib import admin
from .models import college_form, student_form, login
# Register your models here.


admin.site.register(college_form)
admin.site.register(student_form)
admin.site.register(login)