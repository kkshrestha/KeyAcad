from django.contrib import admin
from .models import User, All_course, Certification

class CertificationAdmin(admin.ModelAdmin):
    fields = ('course','certificate_code','course_start','course_comp')

admin.site.register(User)
admin.site.register(All_course)
admin.site.register(Certification, CertificationAdmin)
