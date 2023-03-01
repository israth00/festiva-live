from django.shortcuts import render,redirect
from django.contrib import messages
from musicapp.models import contactdb, registerdb,buydb
from concert.models import categorydb



# Create your views here.
def mainpage(request):
    return render(request,"mainpage.html")

def Ticket(request,dataid):
    data = categorydb.objects.filter(id=dataid)
    print(data)
    return render(request,"BuyTicket.html",{'data':data})



def contactus(request):
    return render(request,"ContactUs.html")

def contactpage(request):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        co = request.POST.get('contact')
        msg = request.POST.get('message')
        messages.success(request, "Added Successfully")
        obj = contactdb(name=na,email=em,contact=co,message=msg)
        obj.save()
        return redirect(contactus)

def discategory(request, itemcatg):

    catg=itemcatg.upper()
    products=categorydb.objects.filter(category=itemcatg)
    context={
        'products':products,
        'catg':catg,

    }

    return render(request,"discategory.html",context)


def aboutus(request):
    return render(request,"AboutPage.html")

def artist(request):
    return render(request,"ArtistPage.html")

def pricing(request):
    data = categorydb.objects.all()
    return render(request,"PricingPage.html",{'data':data})


def schedule(request):
    return render(request,"SchedulePage.html")

def loginhere(request):
    return render(request,"LoginPage.html")



def addregister(request):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        co = request.POST.get('contact')
        messages.success(request, "Registered Successfully")

        obj = registerdb(name=na,email=em,contact=co)
        obj.save()
        return redirect(mainpage)

def ticketsave(request):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        co = request.POST.get('contact')
        qty = request.POST.get('qty')
        pr = request.POST.get('price')
        tt = request.POST.get('total')
        messages.success(request, "Booked Successfully")
        obj = buydb(name=na,email=em,contact=co,quantity=qty,price=pr,total=tt)
        obj.save()
        return redirect(mainpage)