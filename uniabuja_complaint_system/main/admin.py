from django.contrib import admin
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['name', 'complaint', 'sentiment', 'date']
    search_fields = ['name', 'complaint', 'sentiment']
    # list_filter = ['available', 'category', 'paid_for']