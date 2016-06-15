from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import StudentForm

import elasticpy as ep
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
from elasticsearch import Elasticsearch


@csrf_exempt
def create_form(request):
    form = StudentForm(request.POST or None)
    if form is not None:
        es = Elasticsearch()

        if form.is_valid():

            data = {'name': form.cleaned_data['name'], 'analysis': form.cleaned_data['analysis']
                    , 'rno': form.cleaned_data['rno'], 'address': form.cleaned_data['address']}
            es.create('student', doc_type='info', body=data, id=form.cleaned_data['rno'])
            form.save()
            messages.success(request, "record added")
            return HttpResponseRedirect('/student/home/')
    context = {'form': form}
    return render(request, 'create_form.html', context)


def home(request):
    return render(request, 'home.html', {})


def search(request):
    context = {}
    query = ep.ElasticQuery().query_string(query=request.POST['text'])

    sr = ep.ElasticSearch()
    p = sr.search_advanced('student', 'info', query)

    if len(p['hits']['hits']) > 0:
        stu_list = []
        p = sr.return_records('student', 'info', query)

        num = len(p)
        for obj in p:
            stu_list.append(obj['_source'])
            context = {'posts': stu_list, 'count': num}

    return render(request, 'search.html', context)
