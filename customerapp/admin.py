from django.contrib import admin
from customerapp.models import Record

# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email']
