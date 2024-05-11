from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from games.models import GamesModel
from components.models import ComponentsModel
from checkout.models import CartGameItemModel,CartComponentItemModel
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required

User=get_user_model()

# cart needs too many customization so using some function based view instead of 
#class based view.
class UserCart(LoginRequiredMixin,View):
    
    def get(self, request):
        games=CartGameItemModel.objects.filter(buyer=self.request.user.id)
        component=CartComponentItemModel.objects.filter(buyer=self.request.user.id)
        subtotal = sum(item.game.price for item in games)
        subtotal+= sum(item.component.price for item in component)
        context={
            "games":games, 
            "components": component,
            "subtotal":subtotal
        }
        return render(request, "checkout/cart.html",context=context)
        
     

class DemoNoPaymentView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, "checkout/demo_payment.html")

    def post(self, request):
        return render(request, "checkout/demo_payment_error.html")

class PromoCodeView(LoginRequiredMixin,View):
    def post(self,request):
        return redirect("https://i.imgflip.com/3mkotw.jpg")

@login_required
def user_cart_item_count(request):
    try:
        items = CartGameItemModel.objects.filter(buyer=request.user).count() 
        items+= CartComponentItemModel.objects.filter(buyer=request.user).count()
        return HttpResponse(f"<span>{items}</span>")
    except Exception as e:
        return HttpResponse(status=403)

#get the id and type from the url and create a entry in the cart
# url: /usercart/1/game
@login_required
def add_to_cart(request,id,type):

    if type=='game':
        game=GamesModel.objects.get(id=id)
        cart_item, created = CartGameItemModel.objects.get_or_create(buyer=request.user, game=game)
    elif type=='component':
        component=ComponentsModel.objects.get(id=id)
        cart_item, created = CartComponentItemModel.objects.get_or_create(buyer=request.user, component=component)
    return redirect('checkout:usercart')    