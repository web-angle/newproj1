from django.shortcuts import render, redirect
import requests
import json
from main.models import Data


def home_page(request):
	return render(request, 'index.html', {})


def client_credentials(request):
	if request.method == 'POST':
		key1 = request.POST.get('key1')
		key2 = request.POST.get('key2')
	return render(request, 'creds.html', {})


def auth(request):
	return render(request, 'auth.html', {})


def success(request):
	code = request.GET.get('code')
	r = requests.get(f'https://bim360connectorauthcode.azurewebsites.net/api/callback?code={code}&is_local=true')
	data = r.json()
	Data.objects.create(**data)
	return render(request, 'success.html', {})
