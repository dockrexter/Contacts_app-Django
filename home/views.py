from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def redgister(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        form=UserCreationForm()
        args={'form':form}
        return render(request,'home/redg_form.html',args)