import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from analysis.myanalysis import MyAnalysis


def home(request):
    return render(request, 'home.html');


def ws(request):
    year = request.GET['year'];
    month = request.GET['month'];
    print(year, month);
    result = MyAnalysis().wm(int(year), int(month));
    return HttpResponse(json.dumps(result),content_type='application/json');

def ages(request):
    target = request.GET['target'];
    print(target);
    result = MyAnalysis().localage(target);
    print(result)
    return HttpResponse(json.dumps(result),content_type='application/json');

def genders(request):
    target = request.GET['target'];
    result = MyAnalysis().genderage(target);
    print(result);
    return HttpResponse(json.dumps(result),content_type='application/json');

def genders2(request):
    target = request.GET['target'];
    result = MyAnalysis().genderage2(target);
    print(result);
    return HttpResponse(json.dumps(result),content_type='application/json');


def traffics(request):
    station = request.GET['station'];
    line = request.GET['line'];
    result = MyAnalysis().traffics(station, line);
    print(result);
    return HttpResponse(json.dumps(result),content_type='application/json');
