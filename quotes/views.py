from django.shortcuts import render,redirect
# Create your views here.
def home(request):
	import requests
	import json

	if request.method == 'POST':
		pnr = request.POST['pnr']
		url = "https://pnr-status-indian-railway.p.rapidapi.com/pnr-check/"+ str(pnr)
		headers = {
	"X-RapidAPI-Key": "35958a2dd9mshb92df6efcffaefdp117a08jsnf100cac54e6c",
	"X-RapidAPI-Host": "pnr-status-indian-railway.p.rapidapi.com"
}

		api = requests.request("GET", url, headers=headers)

		try:
			api = json.loads(api.content)
		except Exception as e:
			api = "error .. ."	
		return render(request, 'home1.html', {'api':api})
	else:
		return render(request, 'home.html', {'pnr':"wrong pnr"})	
def home1(request):
	import requests
	import json

	if request.method == 'POST':
		pnr = request.POST['pnr']
		url = "https://pnr-status-indian-railway.p.rapidapi.com/pnr-check/"+ str(pnr)
		headers = {
	"X-RapidAPI-Key": "35958a2dd9mshb92df6efcffaefdp117a08jsnf100cac54e6c",
	"X-RapidAPI-Host": "pnr-status-indian-railway.p.rapidapi.com"
}

		api = requests.request("GET", url, headers=headers)

		try:
			api = json.loads(api.content)
		except Exception as e:
			api = "error .. ."	
		return render(request, 'home.html', {'api':api})
	else:
		return render(request, 'home.html', {'pnr':"wrong pnr"})	
