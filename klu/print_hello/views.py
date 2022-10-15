from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def about(request):
    #return HttpResponse("Hello World Example of PFSD Program")
     return render(request,'about.html')

def newuserregister(request):
  if request.method=='POST':

      fname = request.POST['fname']
      name = request.POST['name']
      mail = request.POST['email']
      p1 = request.POST['p1']
      p2 = request.POST['p2']

      contact = request.POST['contact']
      if p1 == p2:
          if User.objects.filter(email=mail).exists():
              messages.info(request, "Already an User with this Email")
              return redirect('newuserregister')
          elif User.objects.filter(username=name).exists():
              messages.info(request, "Already an User with this Username")
              return redirect('newuserregister')
          else:
              user = User.objects.create_user(first_name=fname, email=mail, password=p1, username=name)
              user.save()
              obj = newuserregister(username=name, contact=contact)
              obj.save()
              # subject = "Online Bidding"
              # msg = "Congratulations you are registered successfully."
              # to = mail
              # res = send_mail(subject, msg, "bidmafia007@gmail.com", [to])
              # if res == 1:
              #     return redirect('/')
              # else:
              #     messages.info(request, "Some thing is wrong")
              #     return redirect('register')
      else:
          messages.info(request, "Password does not match")
          return redirect('register')
  else:
      return render(request, 'newuserregister.html')


def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def login(request ):
    # if request.method == 'POST':
    #
    #
    #     user_id=request.POST.get("name")
    #     password=request.POST.get("password")
    #     data= login(user_id=user_id,password=password)
    #     data.save()
    #     return redirect('show/')

    return render(request,'login.html')




def sucess(request):
    return render(request,'sucess.html')

def index(request):
    return render(request,'index.html')

def welcomepage(request):
    return render(request,'welcomepage.html')

def news(request):
    return render(request,'news.html')

def Order(request):
    return render(request,'Order.html')

def billing(request):
    return render(request,'billing.html')

