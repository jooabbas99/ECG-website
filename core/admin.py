from django.contrib import admin

# Register your models here.
from .models import Patient,ECGFile

admin.site.register(Patient)
admin.site.register(ECGFile)
