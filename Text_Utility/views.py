from django.http import HttpResponse

from django.shortcuts import render 

#render takes 3 arguements 3rd are the variables to pass it to the html file

def index(request):
    # params = {'name':'Tushar','place':'Earth'}
    return render(request,'index.html')
    #now params can be accessed by index.html
    # return HttpResponse("INDEX")  

def result(request):
    sitetext =  request.POST.get('text','default')
    params =  {'purpose' : 'You Choose nothing','analyzed_text':"ERROR"}

    RP = request.POST.get('RP','off')
    FC = request.POST.get('FC','off')
    NLR = request.POST.get('NLR','off')
    SR = request.POST.get('SR','off')
    CC = request.POST.get('CC','off')

    if RP == "on":
        params = removepunc(sitetext)
        sitetext = params['analyzed_text']        
    
    if FC == 'on':
        params = fullcapitalize(sitetext)
        sitetext = params['analyzed_text']
    
    if NLR == 'on':
        params = newlineremove(sitetext)
        sitetext = params['analyzed_text']
    
    if SR == "on":
        params = spaceremover(sitetext)
        sitetext = params['analyzed_text']
    
    if CC == "on":
        params = charcount(sitetext)
        sitetext = params['analyzed_text']

    return render(request,"result.html",params)

def removepunc(sitetext):
    
    punctuations = """!`~<>'"@#$%^&*()_+=-[]{};:"""
    analyzed = ""

    for char in sitetext:
        if char not in punctuations:
            analyzed = analyzed + char

    params = {'purpose' : 'Remove Punctuation','analyzed_text':analyzed}
    return params
    # return render(request, 'result.html', params)

    # return HttpResponse("Remove Punctuation" + " in " + sitetext + ''' <a href="http://127.0.0.1:8000/index/">Home Page</a> ''')
#first value is the value we get and the second value is default value

def fullcapitalize(sitetext):
    analyzed = ""
    for char in sitetext:
        analyzed = analyzed + char.upper()

    params = {'purpose' : 'Full Capitalize', 'analyzed_text':analyzed}
    return params

def capatalizefirst(request):
    return HttpResponse("First Capatalization")

def newlineremove(sitetext):
    analyzed = ""
    for char in sitetext:
        if char != "\n" and char != "\r":
            analyzed = analyzed + char

    params = {'purpose' : 'New line removed', 'analyzed_text':analyzed}
    return params

def spaceremover(sitetext):
    analyzed = ""

    for i,char in enumerate(sitetext):
        if sitetext[i] == " " and sitetext[i+1] == " ":
            continue
        analyzed = analyzed + char 

    params = {'purpose' : 'Extra space remover', 'analyzed_text':analyzed}
    return params  

def charcount(sitetext):
    analyzed = ""
    i=0
    j=0

    for char in sitetext:
        i = i+1
        if char == " ":
            j=j+1

    analyzed = "total character count = " + str(i) + " space count = " + str(j)  

    params = {'purpose' : 'Character Count', 'analyzed_text':analyzed}
    return params

def spacecount(request):
    return HttpResponse("Now counting the space")