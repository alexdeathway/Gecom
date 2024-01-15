from django.shortcuts import render
#import view
from django.views.generic import View

class DevelopmentStatusView(View):
      def get(self,request,*args,**kwargs):
          return render(request,"misc/development_status.html",{})