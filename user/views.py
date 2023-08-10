from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to your home page
    else:
        form = UserCreationForm()
    # return render(request,'createSupplier.html',{"form":form})
    return render(request,'register.html',{'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('CreatePartner_url')
    else:
        form = AuthenticationForm()
    return render(request,'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
