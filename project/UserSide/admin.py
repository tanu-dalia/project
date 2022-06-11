from django.contrib import admin

from temp.models import user, user_profile, company, job_applied, job_posting, ResumeModel
# Register your models here.
admin.site.register(user_profile)
admin.site.register(ResumeModel)
