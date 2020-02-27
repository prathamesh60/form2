from django.shortcuts import render,redirect
from app2.forms import *
from app2.models import *

def religion(request):
    if request.method == "POST":
      form1= ReligionForm(request.POST)
      if form1.is_valid():
          try:
              form1.save()
              return redirect("/religion")
          except:
              pass
    else:
        form1= ReligionForm()
        religion1 = Religion.objects.all()
        return render(request,"religion/register.html", {"form1":form1, "religion1": religion1})



def show_religion(request):
    religion1 = Religion.objects.all()

    return render(request, "religion/index.html", {"religion1": religion1} )
def edit(request,id):
    religion2 = Religion.objects.get(RELIGION_NO=id)
    return render(request, "religion/edit.html", { 'religion2':religion2})
def modify_religion(request,id):
    religion2 =Religion.objects.get(RELIGION_NO=id)
    form1 = ReligionForm(request.POST, instance = religion2)
    # religion2.RELIGION_NO = form1.RELIGION_NO
    # religion2.RELIGION_NAME = form1.RELIGION_NAME
    # form1.RELIGION_NO = religion2.A.value#religion2.RELIGION_NO
    # form1.RELIGION_NAME = religion2.B.value#religion2.RELIGION_NAME
    if form1.is_valid():
        form1.save()
        return redirect("/religion")
    return render(request, "religion/edit.html", { 'form1':religion2})
def delete_religion(request,id):
    religion3 =Religion.objects.get(id=id)
    religion3.delete()
    return redirect("/show_religion")
# Create your views here.

# class ClassName(object):
#     # """docstring for ."""
#     model=
