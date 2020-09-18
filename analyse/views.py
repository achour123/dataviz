from django.shortcuts import render
import requests 

# Create your views here.

def analy(request):
    data=True
    result=None
    globalSummary=None
    countries=None
    while(data):
        try:
            result=requests.get('https://api.covid19api.com/summary')
            json=result.json() 
            globalSummary=json["Global"]
            countries=json["Countries"]
            data=False       
        except:
            data=True

        #liste du top 5 deaths#
        l1=list()
        for c in countries:
            l1.append(c['TotalDeaths'])
        l1.sort(reverse=True)
        c=[]
        for j in l1:
            for i in range(len(l1)):
                if countries[i]['TotalDeaths']==j:
                    c.append(countries[i]) 
        s=[]
        for q in range(0,5):
            s.append(c[q])
        l01=list()
        for k in s :
            l01.append(k['TotalDeaths'])
        l02=list()
        for k in s :
            l02.append(k['Country'])    
        ##########################

        #liste du top 5 Confirmed#

        l2=list()
        for k in countries :
            l2.append(k['TotalConfirmed'])
        l2.sort(reverse=True)
        c1=[]
        for j in l2:
            for i in range(len(l2)):
                if countries[i]['TotalConfirmed']==j:
                    c1.append(countries[i])  

        s1=[]
        for q in range(0,5):
            s1.append(c1[q])

        l11=list()
        for k in s1 :
            l11.append(k['TotalConfirmed'])
        l12=list()
        for k in s1 :
            l12.append(k['Country'])
        ##########################
            
        #liste du top 5 Confirmed#

        l3=list()
        for k in countries :
            l3.append(k['TotalRecovered'])
        l3.sort(reverse=True)    
        c2=[]
        for j in l3:
            for i in range(len(l3)):
                if countries[i]['TotalRecovered']==j:
                    c2.append(countries[i]) 

        s2=[]
        for q in range(0,5):
            s2.append(c2[q])

        l21=list()
        for k in s2 :
            l21.append(k['TotalRecovered'])
        l22=list()
        for k in s2 :
            l22.append(k['Country'])    
          
        ##########################        
    

    return render(request,'analyse/analy.html',{'globalSummary':globalSummary,'countries':countries,'l01':l01,'l02':l02,'l11':l11,'l12':l12,'l21':l21,'l22':l22})


