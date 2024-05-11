from django.urls import path
from checkout.views import (DemoNoPaymentView, UserCart,
                            user_cart_item_count, PromoCodeView,
                            add_to_cart,
                            )

app_name="checkout"

urlpatterns = [
    path("nopurchase/",DemoNoPaymentView.as_view(),name="nopurchase"),
    path("usercart/",UserCart.as_view(),name="usercart"),
    path("usercart/<int:id>/<str:type>/",add_to_cart,name="usercart_add"),
    path("usercartitemcount/",user_cart_item_count,name="usercartitemcount"),
    path("promocode/",PromoCodeView.as_view() ,name="promocode"),
]
