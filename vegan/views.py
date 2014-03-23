from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
  context = RequestContext(request)
  context_dict = { 'dish': 'curry' }
  return render_to_response('index.html', context_dict, context)
