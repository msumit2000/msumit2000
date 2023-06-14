from udops.src.dep.ucorpus import *
from udops.src.dep.udataset import *
from udops.src.dep.UserAccessControl import *
from udops.src.dep.Manager.CorpusMetadataManager import *
from udops.src.dep.config.Connection import *
from udops.src.dep.InputProperties import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

#Create your views here.
################# -----------------------------------------------------##################
def get_udops_count(request):
    if request.method=='GET':
        re = ucorpus()
        response=re.get_Counts()
        response_data = {
           "status":"success",
           "data":response
           }
        return JsonResponse(response_data, safe=False)

def get_udops_summary(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        corpus_name = data.get('corpus_name')  # get search_string from data dict
        if corpus_name is None or corpus_name.strip() == '':  # if search_string is null
            response_data = {
                "status": "failure",
                "failure_error": "Input string is null",
            }
            return JsonResponse(response_data, safe=False)
        response = ucorpus.getCorpusMetadata(data['corpus_name'])
        data = json.loads(response)
        response_data = {
        "status": "success",
        "data": data
        }
        return JsonResponse(response_data,safe=False)


@api_view(['POST'])
def get_corpus_list(request):
    re = ucorpus()
    response = re.list_corpus()
    response_data = {
        "status": "success",
        "failure_error": " ",
        "data": response
    }
    return JsonResponse(response_data, safe=False)

@api_view(['POST'])
def search_corpus_by_name(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        search_string = data.get('search_string')  # get search_string from data dict
        if search_string is None or search_string.strip() == '':  # if search_string is null
            response_data = {
                "status": "failure",
                "failure_error": "Input string is null",
            }
            return JsonResponse(response_data, safe=False)
        re = ucorpus()
        response = re.search_corpus(data['search_string'])
        json_string = json.dumps(response)
        data = json.loads(json_string)
        response_data = {
        "status": "success",
        "data": data
         }
        return JsonResponse(response_data, safe=False)
@api_view(['POST'])
def delete_corpus(request):
    data = json.loads(request.body)
    CorpusMetadataManager.delete_corpus(data['corpus_name'],conn)
    return Response("successful")

@api_view(['POST'])
def list_by_string_name(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        search_string = data.get('search_string')  # get search_string from data dict
        if search_string is None or search_string.strip() == '':  # if search_string is null
            response_data = {
                "status": "failure",
                "failure_error": "Input string is null",
               }
            return JsonResponse(response_data, safe=False)
        re = ucorpus()
        response = re.list_by_string(search_string)
        json_string = json.dumps(response)
        data = json.loads(json_string)
        response_data = {
           "status": "success",
           "data": data
         }
        return JsonResponse(response_data, safe=False)

@csrf_exempt
def upsert(request):
    if request.method=='PUT':
        try:
            data= json.loads(request.body)
            corpus = ucorpus()
            if corpus.update_corpus(data)==0 :
                print(corpus.update_corpus(data))
                return JsonResponse({"status":"failure","failure_error":"Corpus doesn't exist"},safe=False)
            elif corpus.update_corpus(data)==1:
                print(corpus.update_corpus(data))
                return JsonResponse({"status":"success"},safe=False)
            elif corpus.update_corpus(data)==2 :
                print(corpus.update_corpus(data))
                return JsonResponse({"status":"failure","failure_error":"corpus_id not belong to corpus_name"},safe=False)
            else:
                print(corpus.update_corpus(data))
                return JsonResponse({"status":"failure","failure_error":"updating same value"},safe=False)
        except Exception as e:
            raise e

def summary(request):
    if request.method =='GET':
        data= json.loads(request.body)
        corpus = ucorpus()
        response=corpus.summary(data['column'])
        print(response)
        data = json.loads(response)
        return JsonResponse(data, safe=False)

def summary_custom(request):
    if request.method =='GET':
        data= json.loads(request.body)
        corpus = ucorpus()
        response=corpus.summary_custom(data["corpus_name"])
        data = json.loads(response)
        return JsonResponse(data, safe=False)

@csrf_exempt
def update_custom_field(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        corpus = ucorpus()
        response = corpus.update_custom_field(data)
        if response ==1:
            return JsonResponse({"status": "updated successfully"}, safe=False)
        else:
            return JsonResponse({"status": "failed"}, safe=False)

@csrf_exempt
def donut(request):
    if request.method =='GET':
        data = ['language','corpus_type','source_type','vendor','domain']
        corpus = ucorpus()
        const_data = []
        i =0
        for i in range(len(data)):
            corpus_property= data[i]
            response=corpus.donut(corpus_property)
            print(response)
            key = response[0]
            value = response[1]
            _data = {'name': f'Per {corpus_property}','labels':key,'dataset': [{'label': ' ','data':f'{value}' }]}
            const_data.append(_data)
            i = i +1
        return JsonResponse(const_data,safe=False)

####################### Dataset API #####################################
def dataset_summary(request):
    if request.method == 'GET':
        data= json.loads(request.body)
        dataset = udataset()
        response = dataset.get_summary(data["dataset_name"])
        print(response)

        json_string = json.dumps(response,ensure_ascii=False)
        j = json.loads(json_string)
        return JsonResponse(j,safe=False)

@csrf_exempt
def dataset_list(request):
    if request.method == 'GET':

        dataset = udataset()
        response = dataset.get_list()
        return JsonResponse(response,safe=False)

@csrf_exempt
def dataset_search(request):
    if request.method == 'POST':
        dataset = udataset()
        data = json.loads(request.body)
        response = dataset.search_dataset(data["property"])
        return JsonResponse(response,safe=False)

@csrf_exempt
def update_dataset(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dataset = udataset()
        response = dataset.update(data["dataset_name"],data["corpus_filter"])
        if response==1:
            return JsonResponse({"status": "updated successfully !!!"}, safe=False)
        else:
            return JsonResponse({"status": "failed"}, safe=False)

def dataset_corpus_list(request):
    if request.method=='GET':
        data = json.loads(request.body)
        dataset = udataset()
        response = dataset.dataset_corpus_list(data["dataset_name"])
        return JsonResponse(response,safe=False)
###********************************************************
## USER MANAGEMENT
def get_user_list(request):
    if request.method=='GET':
        manage = AccessControl()
        response = manage.get_user_list()
        return JsonResponse(response,safe = False)

def update_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        manage = AccessControl()
        response = manage.update_user(data)

        return JsonResponse(response,safe = False)

def get_team_list(request):
    if request.method=='GET':
        manage = AccessControl()
        response = manage.get_team_list()
        return JsonResponse(response, safe=False)
def update_team(request):
    if request.method=='POST':
        data = json.loads(request.body)
        manage = AccessControl()
        response = manage.update_team(data)
        return JsonResponse(response, safe=False)

def add_user_to_team(request):
    if request.method =='POST':
        data = json.loads(request.body)
        manage= AccessControl()
        response = manage.add_user_to_team(data)
        return JsonResponse(response, safe= False)


