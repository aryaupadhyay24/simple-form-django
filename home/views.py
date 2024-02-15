from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import contact_detail

# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')
 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        newdata={
            "name":name,
            "email":email,
            "phone":phone,
            "desc":desc,

        }
        
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        # detail=contact.objects.all()
        # print("measasfg   ",detail)
        data=contact_detail.insert_one(newdata)
        # print("jsnufdsio ",data)
        # contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 