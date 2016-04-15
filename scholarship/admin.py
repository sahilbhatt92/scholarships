from django.contrib import admin
from models import Scholarships
from rest_framework.authtoken.admin import TokenAdmin

"""
Registering Scholarship Model to admin
"""
class ScholarshipAdmin(admin.ModelAdmin):
	fields = ('name', 'amount', 'amount_type', 'end_date')

admin.site.register(Scholarships, ScholarshipAdmin)

TokenAdmin.raw_id_fields = ('user',)
