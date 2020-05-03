from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.conf import settings
from django.urls import reverse
from checkout.forms import DonationForm


import stripe
import os

stripe.api_key = 'sk_test_5UBH6SjTB12sryQRxLTIUfyL00bROW3YcZ'


# Create your views here.





# class CheckoutView(TemplateView):
#     template_name = 'checkout/checkout.html'

#     def get_context_data(self, **kwargs): # new
# 	    context = super().get_context_data(**kwargs)
# 	    context['key'] = settings.STRIPE_PUBLISHABLE_KEY
# 	    return context


@login_required
def checkoutview(request):
	form=DonationForm()

	context={'d_form':form}
    
	return render(request, 'checkout/checkout.html', context )

    

def charge(request): # new
    
    if request.method =='POST':
    	print(request.POST)
    	token=request.POST['stripeToken']
    	amount=int(request.POST['amount'])
    	

    	customer=stripe.Customer.create(
    		
    		email=request.POST['email'],
    		name=request.POST['name'],
    		source=request.POST['stripeToken']
    		
    		)

    	stripe.Charge.create(
    		customer=customer,
    		amount=amount*100,
    		currency="usd",
    		description=f"{amount}usd Donation!!",
)

    return redirect(reverse('success', args=[amount]))



def successMsg(request, args):
    amount =args
    return render(request, 'checkout/success.html', {'amount':amount})

@login_required
def premium(request):
	context={}
	return render(request, 'checkout/premium.html', context)
@login_required
def subcheckoutview(request, amount):

	context={'amount':amount}
	return render(request, 'checkout/subcheckout.html', context)