# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from plotmap.models import *
import json

def home(request):
	data=location.objects.get(id=1)
	variables = RequestContext(request, {'data' : data,'user':request.user})
     	template='home.html'
     	return render_to_response(template, variables)
def getPath(request,id):
	path.objects.filter(id=id)
	if path:
		path1=path.objects.get(id=id)
		data=path1.pathid.all()[0]
		variables = RequestContext(request, {'data' : data,'user':request.user})
     		template='home.html'
     		return render_to_response(template, variables)
		
def getLocation(request,incr=0):
	if request.is_ajax():
		incr=request.POST.get('incr', False)
		incr=int(incr)+1
		id1=request.POST.get('id', False)
	path1=path.objects.get(id=id1)
	data=data=path1.pathid.all()
	dic={}
	len1=len(path1.pathid.all())
	print len1
	lst=[]
	if (incr < len1):
		data=path1.pathid.all()[incr]
		dic['id']=data.id
		dic['incr']=incr
		dic['name']=data.name
		dic['lat']=float(data.lat)
		dic['long']=float(data.lang)
		return HttpResponse(json.dumps(dic))
	else:
		return HttpResponse("Finished")
		
		
	
def getAllPath(request,incr=0):
        path1=path.objects.all()[0]
        path2=path.objects.all()[1]
        path3=path.objects.all()[2]
        data1=path1.pathid.all()[0]
        data2=path2.pathid.all()[0]
        data3=path3.pathid.all()[0]
        lst=[]
        alldata=path.objects.all()
        print "Hello",request.user
        if request.is_ajax():
                incr=request.POST.get('incr', False)
                incr=int(incr)+1
                for each in alldata:
                        if (incr< len(each.pathid.all())):                
                                data=each.pathid.all()[incr]
                                dic={}
                                dic['id']=data.id
                                dic['incr']=incr
                                dic['name']=data.name
                                dic['lat']=float(data.lat)
                                dic['long']=float(data.lang)
                                dic['pathid']=each.id
                                lst.append(dic)
                return HttpResponse(json.dumps(lst))
        variables = RequestContext(request, {'path1' : data1,'path2' : data2,'path3' : data3,'user':request.user})
     	template='GetAllPAth.html'
     	return render_to_response(template, variables)               
