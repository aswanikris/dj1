from django.shortcuts import render,redirect
from.forms import todoform
from.models import tab
# Create your views here.
def fun(request):
    form=todoform()
    t=tab.objects.all()
    if request.method=='POST':
        form=todoform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'index.html',{'fo':form,'todo':t})

def update(request,todo_id):
    todo=tab.objects.get(id=todo_id)
    form=todoform(instance=todo)
    if request.method=='POST':
        form=todoform(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('fun')
    return render(request,'update.html',{'form':form})
    
def delete(request,todo_id):
    if request.method=='POST':
        tab.objects.get(id=todo_id).delete()
        return redirect('fun')
    
        
    
