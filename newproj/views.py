from django.shortcuts import render, redirect
import requests
import json
from main.models import Data


def home_page(request):
	# r = requests.get('https://cdn.liftoff.shop/docs/po.xml')
	# print('request: ', r)
	return render(request, 'index.html', {})


def client_credentials(request):
	if request.method == 'POST':
		key1 = request.POST.get('key1')
		key2 = request.POST.get('key2')
		print(key1)
		print(key2)
	return render(request, 'creds.html', {})


def auth(request):
	return render(request, 'auth.html', {})


def success(request):
	code = request.GET.get('code')
	Data.objects.create(code=code)
	# r = requests.get(f'https://bim360connectorauthcode.azurewebsites.net/api/callback?code={code}&is_local=true')
	return render(request, 'success.html', {'code': code, 'data': None})


def success1(request):
	token = request.GET.get('code')
	d = {'abc': 'aaa', 'xyz': 'aaa'}
	code = Data.objects.get(code=token)
	r = requests.get(f'https://bim360connectorauthcode.azurewebsites.net/api/callback?code={code}&is_local=true')
	return render(request, 'success1.html', {'data': r.json()})









	# mine: gettoken
	# url = f"https://developer.api.autodesk.com/authentication/v1/gettoken?code={code}&client_id=QfFDg8lZnaIA5ETChbeDTQzPvti7Qzxs&client_secret=ogu0qlrK3PMgPIj6&grant_type=authorization_code&redirect_uri=http://9744262a36b9.ngrok.io/success&scope=data:read"
	# headers = {'content-type': 'application/x-www-form-urlencoded'}
	# r = requests.post(url, data={}, headers=headers)