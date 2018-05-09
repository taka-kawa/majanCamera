from django.shortcuts import render
from django.http import HttpResponse
import os
import json

def pull(request):
    if request.method == 'POST':
        print(os.system('git pull origin master'))
        res = {
                "message":"ok"
              }
        result = json.dumps(res)
        return HttpResponse(result, content_type='application/json')


    error_res = {
                  "error":{
                    "message":"error"
                  }
                }
    result = json.dumps(error_res)
    return HttpResponse(result, content_type='application/json', status=400)