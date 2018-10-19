from django.contrib import admin
from .models import *

class DocumentAdmin(admin.ModelAdmin):
	fields = ['document', 'description', 'uploaded_at']
	list_display = ['document', 'description', 'uploaded_at']
	list_filter = ['document']
	
admin.site.register(Document, DocumentAdmin)
