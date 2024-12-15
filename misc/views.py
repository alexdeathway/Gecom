from django.shortcuts import render
#import view
from django.views.generic import View,TemplateView

class DevelopmentStatusView(View):
      def get(self,request,*args,**kwargs):
          return render(request,"misc/development_status.html",{})

class Error404TestView(TemplateView):
    template_name = "errors/404.html"

class Error500TestView(TemplateView):
    template_name = "errors/500.html"
