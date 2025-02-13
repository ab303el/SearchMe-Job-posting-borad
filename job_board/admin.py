from django.contrib import admin
from .models import jobPosting , jobcategories

# Register your models here.
admin.site.register(jobPosting)
admin.site.register(jobcategories)