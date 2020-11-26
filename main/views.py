from django.shortcuts import render
from django.conf import settings

import requests
# Create your views here.

def github(request):
	user = {}
	if 'username' in request.GET:
		username = request.GET['username']
		url = 'https://api.github.com/users/%s' % username
		response = requests.get(url)
		user = response.json()
		#print(user)

	return render(request, 'home.html', {'user':user})


'''
def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        
        user = response.json()
        
        
    return render(request, 'home.html', {'user': user})
'''