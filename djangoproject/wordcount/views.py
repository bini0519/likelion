from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dict = {}
    for a in words:
        if a in word_dict:
            #increase
            word_dict[a] += 1
        else:
            #add
            word_dict[a] = 1


    return render(request, 'result.html', {'full' : text, 'total' : len(words), 'dict' : word_dict.items})