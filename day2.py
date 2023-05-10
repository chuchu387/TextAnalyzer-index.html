# pipeline in django

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    removepun = request.POST.get('text', 'default')

    #check the checkbox value
    djtext = request.POST.get('check', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charactercounter = request.POST.get('charactedcounter', 'off')

    # print(djtext)
    # print(removepun)



    # check which checkbox is on
    if (djtext == "on"):
        puncutations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~ '''
        analyzed = ""
        for char in removepun:
            if char not in puncutations:
                analyzed = analyzed + char
        params = {'Purposed': 'Removed puncutations', 'analyzed_text': analyzed}
        # analyzed the text
        return render(request, 'analyze.html', params)


    elif(fullcaps == 'on'):
        analyzed = ""
        for char in removepun:
            analyzed = analyzed + char.upper()
        params = {'Purposed': 'Changed To uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif(newlineremover == 'on'):
        analyzed = ""
        for char in removepun:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"Purposed": "Remove New Lines", "analyzed_text": analyzed}
        return render(request, 'analyze.html', params)
    # if(djtext != "on" and fullcaps != "on" and newlineremover != "on"):
    #     return HttpResponse('''Error <br> <a href= "http://127.0.0.1:8000/">Back to Home</a>''')


    elif(charactercounter == 'on'):
        analyzed = ""
        for char in removepun:
            analyzed = len(removepun)
        params = {"Purposed": "character count of your number is: ", "analyzed_text": analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('''Error <br> <a href= "http://127.0.0.1:8000/">Back to Home</a>''')

# day3
# def Capatalizefirst(request):
#     return HttpResponse('''capfirst <br> <a href= "http://127.0.0.1:8000/">Back to Home</a>''')
#
# def newlineremove(request):
#     return HttpResponse('''newlineremove <br> <a href= "http://127.0.0.1:8000/">Back to Home</a>''')
#
# def spaceremove(request):
#     return HttpResponse('''spaceremove <br> <a href= "http://127.0.0.1:8000/">Back to Home</a>''')
#
# def charcount(request):
#     return HttpResponse('''charcount <br> <a href= "http://127.0.0.1:8000/">Back to Home</a>''')
