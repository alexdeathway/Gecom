from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from games.models import GamesModel
from components.models import ComponentsModel
from checkout.models import CartGameItemModel,CartComponentItemModel
from django.contrib.auth import get_user_model

User=get_user_model()
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

    def post(self, request):
        id = request.POST.get('id')
        type=request.POST.get('type')
        if type=='game':
            game=GamesModel.objects.get(id=id)
            cart_item, created = CartGameItemModel.objects.get_or_create(buyer=request.user, game=game)
        elif type=='component':
            component=ComponentsModel.objects.get(id=id)
            cart_item, created = CartComponentItemModel.objects.get_or_create(buyer=request.user, component=component)
            pass
        
        #this can be used if trying to order multipe of same
        # if not created:
        #     item.count+=1
        
        return redirect('checkout:usercart')

    def delete(self, request):
        id = request.POST.get('id')
        type=request.POST.get('type')
       # user=User.objects.get(username=request.user.username)
        if type=='game':
            game=CartGameItemModel.objects.get(buyer=self.request.user, id=id)
            game.delete()
        elif type=='component':
            
            component=CartComponentItemModel.objects.get(buyer=request.user, id=id)
            component.delete()
        return redirect('checkout:usercart')

    def dispatch(self, *args, **kwargs):
        """
        can't send delete method directly from html form ,
        So, wrapped it in post request
        """
        method = self.request.POST.get('_method', '').lower()
        if method == 'get':
            return self.get(*args, **kwargs)
        elif method == 'post':
            return self.post(*args, **kwargs)
        elif method == 'delete':
            return self.delete(*args, **kwargs)
        return super(UserCart, self).dispatch(*args, **kwargs)


class DemoNoPaymentView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, "checkout/demo_payment.html")

    def post(self, request):
        return render(request, "checkout/demo_payment_error.html")

class PromoCodeView(LoginRequiredMixin,View):
    def post(self,request):
        return redirect("https://i.imgflip.com/3mkotw.jpg")

def user_cart_item_count(request):
    try:
        items = CartGameItemModel.objects.filter(buyer=request.user).count() 
        items+= CartComponentItemModel.objects.filter(buyer=request.user).count()
        return HttpResponse(f"<span>{items}</span>")
    except Exception as e:
        return HttpResponse(status=403)

