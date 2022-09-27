import re
from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here
def showformdata(request):
    fm = StudentRegistration(auto_id=True,label_suffix='')
    fm.order_fields ( field_order = ['email','name' ] )

    return render(request ,'student/info.html',{'form':fm})
