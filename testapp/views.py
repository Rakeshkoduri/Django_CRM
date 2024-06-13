from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Register, AddRecordForm
from .models import Record


# Create your views here.

def home(request):
    records = Record.objects.all()
    context = {
        'records': records,
    }

    return render(request, 'testapp/index.html', context)


def about(request):
    return render(request, 'testapp/about.html', )


def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'register successfully')
            return redirect('home')
    else:
        form = Register()
        context = {
            'form': form
        }
        return render(request, 'testapp/register.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in")
            return redirect('home')
        else:
            messages.success(request, ' There was an a error')
            return redirect('register')
    else:
        return render(request, 'testapp/login_page.html')


def logout_page(request):
    logout(request)
    messages.success(request, ' You have been logged out...')
    return redirect('login_page')


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        context = {
            'customer_record': customer_record
        }
        return render(request, 'testapp/record.html', context)
    else:
        messages.success(request, ' You have to Log_in First to view the Record')
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record delete successfully')
        return redirect('home')
    else:
        return redirect('about')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                return redirect("home")

        context = {
            'form': form,
        }
        return render(request, 'testapp/add_record.html', context)
    else:
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form,
        }
        return render(request, 'testapp/update_record.html', context)
    else:
        return redirect('home')
