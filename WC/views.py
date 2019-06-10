from django.shortcuts import render
import re
# Create your views here.

def home(request):
    return render(request, 'WC/home.html')

def about(request):
    return render(request, 'WC/about.html')

def result(request):
    text = request.GET['fulltext']
    words = re.split('\W+', text)
    # words = text.split()
    # 기준에 따라 text를 자름!
    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        
        else:
            word_dict[word] = 1

    return render(request, 'WC/result.html', {'full': text, 'total':len(words), 'dict' : word_dict.items(),})