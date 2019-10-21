from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import urllib.parse
import json
from django.http import JsonResponse
# Create your views here.

@csrf_exempt
def login(request):
    if request.method == 'POST':
        form_data = request.POST
        try:
            microservices_url = 'http://microservices:8000/api/v1/login'
            encoded_form_data = urllib.parse.urlencode(form_data).encode('utf-8')
            request2 = urllib.request.Request(microservices_url, data=encoded_form_data, method='POST')
            json_respsonse = urllib.request.urlopen(request2).read().decode('utf-8')
            response = json.loads(json_respsonse) # redundant?
            return HttpResponse(json.dumps(response))
            
        except Exception as error:
            return JsonResponse({"Experience Service Register Error Message": str(error)})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form_data = request.POST
        try:
            microservices_url = 'http://microservices:8000/api/v1/person/create'
            encoded_form_data = urllib.parse.urlencode(form_data).encode('utf-8')
            request2 = urllib.request.Request(microservices_url, data=encoded_form_data, method='POST')
            json_respsonse = urllib.request.urlopen(request2).read().decode('utf-8')
            response = json.loads(json_respsonse) # redundant?
            return HttpResponse(json.dumps(response))
            
        except Exception as error:
            return JsonResponse({"Experience Service Register Error Message": str(error)})


@csrf_exempt
def home(request):

    req = urllib.request.Request(
        'http://microservices:8000/api/v1/newest_items')

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return JsonResponse(resp)


@csrf_exempt
def item(request, item_id):
    req = urllib.request.Request(
        'http://microservices:8000/api/v1/furniture/'+str(item_id))

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return JsonResponse(resp)
