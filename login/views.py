from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse

class IndexClass(View):
    def get(self, req):
        return HttpResponse("helo world")

