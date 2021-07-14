from django.shortcuts import render
from django.views import View
# Create your views here.

class IndexClass(View):
    def get(self, req):
        like = ["ổi", "Xoài", "Vải", "Sầu riêng"]
        a = {"name": "Vo Dac Vuong", 'lisL': like}
        return render(req, "poll/index.html", a)
