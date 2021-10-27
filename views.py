# CREATED
from django.http import HttpResponse
from django.shortcuts import render

with open(r"C:\Users\Dell\PycharmProjectsHtmlTuts\tut5_Forms.html", "r") as html_file:
    code = html_file.readlines()  # iss code ko response me daal ke dekho html code run ho jaayega


def index(request):
    params = {
        'name': 'harry',
        'place': 'Mars'
    }
    return render(request, 'index.html', params)


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    # Check which checkbox is checked
    if removepunc == "on":
        punctuations = ''':;()'",<>!@#$%^&*_~[]{}?/'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {
            'purpose': 'Removed Punctuations',
            'analyzed_text': analyzed
        }

        djtext = analyzed

    if fullcaps == "on":

        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {
            'purpose': 'Changed To UPPERCASE',
            'analyzed_text': analyzed
        }

        djtext = analyzed

    if newlineremover == "on":

        analyzed = ""
        for char in djtext:

            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {
            'purpose': 'Removed New Lines',
            'analyzed_text': analyzed
        }

        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):

            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {
            'purpose': 'Removed Spaces',
            'analyzed_text': analyzed
        }

        djtext = analyzed

    if charcounter == "on":
        chars = 0
        for char in djtext:
            chars += 1

        analyzed = f"Your Text - {djtext} - Contains {chars} Characters"

        params = {
            'purpose': 'Character Counted',
            'analyzed_text': analyzed
        }

    # Handles error
    if removepunc != "on" and newlineremover != "on" and charcounter != "on" and extraspaceremover != "on" \
            and fullcaps != "on":
        params = {'text': djtext}
        return render(request, 'error.html', params)

    return render(request, 'analyze.html', params)
