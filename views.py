from django.shortcuts import render,redirect,get_object_or_404
from app1.models import UserModel,LoginModel,GymDetails,QueryModel,UserRequest
from gymmanager.models import TrainerDetails,GymDetails
from django.contrib import messages
from app1.form import Userform





def home(request):

    return render(request,"index.html")

def register(request):
    f=Userform()
    fff={"ff":f}


    return render(request,"register.html",fff)

def checkregister(request):
    uid=request.POST.get('uid')
    n=request.POST.get("name")
    a = request.POST.get("age")
    c = request.POST.get("contact")
    g= request.POST.get("gender")
    u = request.POST.get("username")
    p=request.POST.get("password")

    f=Userform(request.POST)
    if f.is_valid():
        UserModel(uid=uid,name=n, age=a, contact=c, gender=g, username=u,password=p).save()
        LoginModel(username=u,password=p).save()
        messages.success(request, "user saved Succefully")

        return redirect('register')
    else:
        return render(request,"register.html",{"ff":f})






def userlogin(request):

    return render(request,"userlogin.html")
def checklogin(request):
    un = request.POST.get('t1')
    pa = request.POST.get('t2')

    try:
         check=UserModel.objects.get(username=un,password=pa)
         request.session['uid'] =check.uid
         request.session['username'] = check.username
         return render(request,"usernavbar.html",{"name":un})
    except UserModel.DoesNotExist:
        messages.error(request,"invalid user")
        return redirect('register')

def fgpassword(request):
    return render(request,"fgpassword.html")

def showgym(request):
    item = GymDetails.objects.all()
    return render(request, "showgym.html", {"items": item})

def showtrainer(request):
    d=TrainerDetails.objects.all()
    td={"td":d}
    return render(request,"showtrainer.html",td)

def anyquery(request):
    return render(request,"anyquery.html")


def savequery(request):
    un= request.POST.get('t1')
    qu = request.POST.get('t2')
    QueryModel(username=un,query=qu).save()
    messages.error(request, "QUERY ADDED SUCCESFULLY")
    return redirect('anyquery')
def showpassword(request):
    una=request.POST.get('p1')
 #   cno = request.POST.get('p2')
    try:
        UserModel.objects.get(username=una)
        res=LoginModel.objects.get(username=una)
        return render(request,"fgpassword.html",{"Error":res.password})
    except UserModel.DoesNotExist:
        return render(request,"fgpassword.html",{"message":'invalid details'})
def userrequest(request):
    noo=request.GET.get('no')
    userid=request.session['uid']
    userObj=UserModel.objects.get(uid=userid)
    gymObj=GymDetails.objects.get(gid=noo)
    UserRequest.objects.create(userId=userObj,gymId=gymObj)
    return redirect('requeststatus')

def requeststatus(request):
    userid = request.session['uid']
    userj = UserModel.objects.get(uid=userid)
    objs=UserRequest.objects.filter(userId=userj)
    return render(request,'requeststatus.html',{'objectss':objs})


def usernvbar(request):

    return render(request,"usernavbar.html")