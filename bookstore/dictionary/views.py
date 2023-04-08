from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.

# Home page for dictionary app
def homeView(request):
    return render(request, 'dictionary/index.html')

# Search page for dictionary
def searchView(request):
    word = request.GET.get('search')
    dictionary = PyDictionary()
    meanings = dictionary.meaning(word)
    synonyms = dictionary.synonym(word)
    antonyms = dictionary.antonym(word)
    context = {
        'word': word,
        'meanings': meanings,
        'synonyms': synonyms,
        'antonyms': antonyms,
    }
    return render(request, 'dictionary/search.html', context)