from django.shortcuts import render
from .forms import Contactform
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponse
class ContactFormView(FormView):
    template_name='school/contact.html'
    form_class= Contactform
    success_url='/thankyou/'
    def form_valid(self,form):
        # print(form)
        print(form.cleaned_data['email'] )
        print(form.cleaned_data['name'] )
        print(form.cleaned_data['message'] )
        return HttpResponse('msg sent')

class ThanksTemplateView(TemplateView):
    template_name ='school/thankyou.html'
