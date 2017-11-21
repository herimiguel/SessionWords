from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import datetime, time

# Create your views here.

def index(request):
    if 'show' not in request.session:
        request.session['show'] = []
    context = { 
        'show' : request.session['show']
    }
    return render(request, 'my_app/index.html', context)

def submit_word(request):
    if 'word' not in request.POST:
        return redirect('/')
    else:
        word =request.POST['word']
    if 'color' in request.POST:
        color = request.POST['color']
    else:
        color = 'white'   
    if 'font' in request.POST:
        largeFont = 10
    else:
        largeFont = 5
    new_word = {
            'word' : word,
            'color' : color,
            'largeFont' : largeFont,
            # 'display_time': time.datetime.now()
            # "display_time" : time.strftime('%a %H:%M:%S')
            "display_time" : time.strftime("%m-%d-%Y-%H:%M %p")
            
    }
    request.session['show'].append(new_word)
    request.session.modified = True
    return redirect('/')

def result(request):
    return render(request, 'my_app/index.html')

def clear(request):
    request.session.clear()
    return redirect('/')

    

