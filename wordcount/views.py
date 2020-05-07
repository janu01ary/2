from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    myText = request.GET['fulltext']
    words = myText.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full': myText, 'total': len(words), 'dictionary': word_dictionary.items()})