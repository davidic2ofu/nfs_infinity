from django import forms
from nfs.models import Document

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ('description', 'document', )