from django.shortcuts import render

import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipedia
# import webbrowser

def index(request):
    return render(request, 'webqueryfinder/index.html')
def search(request):
    query = request.GET.get('query')

    try:
        client = wolframalpha.Client("X4GXWV-9ETJLHU7XY")
        result = client.query(query)
        answer = next(result.results).text
        return render(request, 'webqueryfinder/index.html', {'answer': answer, 'query': query})

            
    except Exception:
        try:
            answer = wikipedia.summary(query, sentences=10)
            return render(request, 'webqueryfinder/index.html', {'answer': answer, 'query': query})


        except Exception:
            answer = "Sorry! We can not find the result."
            return render(request, 'webqueryfinder/index.html', {'answer': answer, 'query': query})