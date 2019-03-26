from django.shortcuts import render
from json import load
from fuzzywuzzy.process import extract
from django.http import JsonResponse

# Create your views here.-------------------------------------------------------
with open('words_dictionary.json', 'r') as f:
	distros_dict = load(f)
f.close()


def index(req):
	return render(req, 'index.html')


def search(req):
	global distros_dict
	search_word = req.GET['keyword']
	a = [key for key, value in distros_dict.items() if search_word in key.lower()]
	
	result = dict(extract(search_word, a, limit=25))
	sortedlist = list(dict(sorted(result.items(), key=lambda s: len(s[0]))).keys())
	
	return JsonResponse({'result': sortedlist})
