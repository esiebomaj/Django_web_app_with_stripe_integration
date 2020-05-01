from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.conf import settings
from django.urls import reverse

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.





# class CheckoutView(TemplateView):
#     template_name = 'checkout/checkout.html'

#     def get_context_data(self, **kwargs): # new
# 	    context = super().get_context_data(**kwargs)
# 	    context['key'] = settings.STRIPE_PUBLISHABLE_KEY
# 	    return context


@login_required
def checkoutview(request):
    context={}
    return render(request, 'checkout/checkout.html', context)

    

def charge(request): # new
    amount=5
    if request.method =='POST':
        print('data : ', request.POST)

    return redirect(reverse('success', args=[amount]))



def successMsg(request, args):
    amount =args
    return render(request, 'checkout/success.html', {'amount':amount})