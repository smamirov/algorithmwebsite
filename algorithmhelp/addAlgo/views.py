from django.shortcuts import render, redirect
from .forms import addAlgorithmForm
from .models import addAlgorithm
from django.contrib import messages

# Create your views here.
def addAlgo(request):
    form = addAlgorithmForm(request.POST or None)
    if form.is_valid():
        form.save() 
        messages.success(request, "Successfully Added!")
        form = addAlgorithmForm()
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'addalgo.html', context)


def displayAlgo(request, id):
    data_id = int(id)
    data = addAlgorithm.objects.get(id=data_id)

    context = data
    return render(request, "displayalgo.html", {"specificData": context})

def viewAlgo(request):
    data = addAlgorithm.objects.all()
    return render(request, 'viewalgo.html', {'all': data})

def changeAlgo(request, id):
    data_id = int(id)
    data = addAlgorithm.objects.get(id=data_id)
    form = addAlgorithmForm(instance=data)

    if request.method == "POST":
        form = addAlgorithmForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/viewalgo')
    context = {'form': form}
    return render(request, "changealgo.html", context)

def deleteAlgo(request, id):
    data_id = int(id)
    data = addAlgorithm.objects.get(id=data_id)
    if request.method == "POST":
        data.delete()
        return redirect("/viewalgo")
    
    context = {"algorithm": data}
    return render(request, "deletealgo.html", context)

    


