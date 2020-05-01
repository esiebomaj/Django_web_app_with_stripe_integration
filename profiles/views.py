from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . forms import ContactForm
from django.core.mail import send_mail

# Create your views here.


def Home(request):
	return render(request, 'profiles/home.html')


def aboutview(request):
	context={}
	return render(request, 'profiles/about.html', context)

@login_required
def profileview(request):
	user=request.user
	context={}
	return render(request, 'profiles/profile.html', context)


def contactview(request):
	user=request.user
	form=ContactForm()
	success_text=None
	context={'form':form, 'message':success_text}
	if request.method =='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			name=form.cleaned_data['name']
			email=form.cleaned_data['email']
			comment=form.cleaned_data['comment']
			message='Name : {} Email : {} comment : {}'.format(name, email, comment)

			send_mail('Message form my site JeremAIh',
				message,
				email,
				['esiebomaj@gmail.com'],
				fail_silently=False,)
			success_text='We have recieved your feedback we will get back to you shortly'
			form=None
			context={'form':form, 'message':success_text}
	return render(request, 'profiles/contact.html', context)



