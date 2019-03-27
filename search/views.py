from django.shortcuts import render
from json import load
from fuzzywuzzy.process import extract
from django.http import JsonResponse
from os import getcwd
import re
# Create your views here.-------------------------------------------------------
with open(getcwd()+'/fuzzy_word_search/words_dictionary.json', 'r') as f:
	distros_dict = load(f)
f.close()


def index(req):
	return render(req, 'index.html')

def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = '.*?'.join(user_input)   # Converts 'djm' to 'd.*?j.*?m'
    regex = re.compile(pattern)  # Compiles a regex.
    for item in collection:
        match = regex.search(item)   # Checks if the current item matches the regex.
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(suggestions)]

def search(req):
	global distros_dict
	search_word = req.GET['keyword'].lower()
	a = [key for key, value in distros_dict.items() if search_word in key]
	a = fuzzyfinder(search_word, a)

	result = dict(extract(search_word, a, limit=25))
	sortedlist = list(dict(sorted(result.items(), key=lambda s: len(s[0]))).keys())

	return JsonResponse({'result': sortedlist})
