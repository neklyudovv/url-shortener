from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import url as urlModel
import random as rand

# Create your views here.
def generate(request, longUrl):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	numbers = '0123456789'
	result = ''
	for i in range(0, 8):
		if rand.randint(0, 2) == 0:
			result += alphabet[rand.randint(0, 26)]
		else:
			result += numbers[rand.randint(0, 9)]
	if len(urlModel.objects.filter(shortUrl=result)) == 0:
		url = urlModel()
		url.longUrl = longUrl
		url.shortUrl = result
		url.save()
		return f'Successful! Share your link - <a href="localhost:8000/{result}">localhost:8000/{result}</a>.'


def index(request):
	response = ''

	if request.method == 'POST':
		response = generate(request, request.POST.get('longUrl'))

	context = {
		'response' : response,
	}
	return render(request, 'index.html', context)


def redirect(request, short):
	urls = urlModel.objects.filter(shortUrl=str(short))
	if len(urls) != 0:
		return HttpResponseRedirect(urls[0].longUrl)
	return HttpResponse('<html><head><title>404 page</title></head><body><p align="center"style="margin-top: 5%;">Couldnt find a link, 404</p></html>')