from django.shortcuts import render
from django.http import HttpResponse
from covichecker.modelpred import *
 

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def prediction(request):
    return render(request,'predict.html')

def helpcenter(request):
    return render(request,'helpcenter.html')

def covid(request):
     #cough
    val1=request.POST.get('v1','no').lower()
    #fever
    val2=request.POST.get('v2','no').lower()
    #sore-throat
    val3=request.POST.get('v3','no').lower()
    #shortness-of-braethe
    val4=request.POST.get('v4','no').lower()
    #headache
    val5=request.POST.get('v5','no').lower()
    #age-60-and-above (0,1)
    val6=request.POST.get('v6','no').lower()
    #gender (0,1)
    val7=request.POST.get('v7','no').lower()
    #test-indication (0,1,2)
    val8=request.POST.get('v8','no').lower().lower().replace(" ", "")

    if 'yes' in (val1, val2, val3, val4, val5, val6):
        val1=val2=val3=val4=val5=val6=1
    elif 'no' in (val1,val2,val3,val4,val5,val6):
        val1=val2=val3=val4=val5=val6=0

    if val7=='male':
        val7=1
    elif val7=='female':
        val7=0

    if val8=='other':
        val8=0
    elif val8=='contactwithconfirmed':
        val8=1
    elif val8=='abroad':
        val8=2

    form_values=[[val1,val2,val3,val4,val5,val6,val7,val8]]

    covid_pred=covid_result_pred(form_values)
    separator=','

    if covid_pred=='positive':
        covid_pred='Positive'
        covid_details='Your test result is Positive, which means there is a high chance of you contracting the virus. Contact your nearest hospital and try to remain isolated from your family members, especially your elders.'
    else:
        covid_pred='Negative'
        covid_details='Your test result is Negative. But it is better to be safe than sorry! Always wear a mask in public places and try to maintain safe distance from others and wash your hands often. Remember only together, we can defeat this pandemic.'
    
    params={'covid_result':covid_pred,'detail':covid_details}
       

    return render(request,'result.html',params)
