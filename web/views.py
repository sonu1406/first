from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')
def count(request):
    textread=request.GET['textread']
    wordcount=textread.split()
    worddictionary={}
    for i in wordcount:
        if i in worddictionary:
            worddictionary[i]+=1
        else:
            worddictionary[i]=1
    sordict=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':textread,'count':len(wordcount),'sordict':sordict})
