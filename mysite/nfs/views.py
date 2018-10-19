from django.shortcuts import render, redirect, get_object_or_404
import os, zipfile
from io import StringIO
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from nfs.forms import DocumentForm
from nfs.models import *
from mysite import settings

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			return redirect('login')
	else:
		return redirect('login')
	
def index(request):
	document_list = Document.objects.all()
	context = {'document_list': document_list}
	if request.method == 'POST':
		if 'chdir' in request.POST:
			print('change directory')
		elif 'getone' in request.POST:
			if 'document' in request.POST:
				values = request.POST.getlist('document')
				path = str(Document.objects.get(pk=values[0]).document)
				file_path = os.path.join(settings.MEDIA_ROOT, path)
				if os.path.exists(file_path):
					with open(file_path, 'rb') as fh:
						response = HttpResponse(fh.read(), content_type='application/force-download')
						response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
						return response
		elif 'getall' in request.POST:
			if 'document' in request.POST:
				values = request.POST.getlist('document')
				zip_path = os.path.join(settings.MEDIA_ROOT, 'docs.zip')
				with zipfile.ZipFile(zip_path, 'w') as myzip:
					for val in values:
						doc_name = str(Document.objects.get(pk=val).document)
						doc_path = os.path.join(settings.MEDIA_ROOT, doc_name)
						myzip.write(doc_path, doc_name)
				myzip.close()
				with open(zip_path, 'rb') as fh:
					response = HttpResponse(fh.read(), content_type='application/force-download')
					response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(zip_path)
					return response
			print('get all documents')
		elif 'delete' in request.POST:
			values = request.POST.getlist('document')
			for v in values:
				d = Document.objects.get(id=v)
				d.delete()
			print(values)
		
		print(request.POST)
	return render(request, 'nfs/index.html', context)
	
def upload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/nfs/index')
	else:
		form = DocumentForm()
	context = {'form': form, }
	return render(request, 'nfs/upload.html', context)