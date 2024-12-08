from django.shortcuts import render,redirect
from django.views import View
from .models import User
from django.contrib.auth import authenticate, login , logout
from .forms import Signup_form, Profile_edit_form
from django.contrib.auth.mixins import LoginRequiredMixin
from Inventory.models import Product

class signin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request,'signin.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists() :
            return render(request,'signin.html',{'error1':' not found','color1':'red'})

        user = authenticate(username=username, password=password)
        if user is None:
            return render(request,'signin.html',{'error2':'Invalid ', 'color2':'red','name':username})
        
        login(request, user)
        return redirect('dashboard')
        

class signup(View):
    def get(self, request):
        return render(request,'signup.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')

        if User.objects.filter(username = username).exists():
            context={
                'status':'Username already exists',
                'data':request.POST
                }
            return render(request,'signup.html',context)

        if password != re_password:
            context={
                'status':'Passwords unmatched',
                'data':request.POST
                }
            return render(request,'signup.html',context)
        
        form = Signup_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('signin')
        
        context={
            'status':'Oops! Something went wrong. Please try again.',
            'data':request.POST
        }
        return render(request,'signup.html',context)

class dashboard(View):
    def get(self, request):
        context={
            'items': Product.objects.all()
        }
        return render(request,'dashboard.html',context)

class signout(LoginRequiredMixin,View):
    login_url = 'signin'
    def get(self, request):
        logout(request)
        return redirect('dashboard')
    
class profile(LoginRequiredMixin,View):
    login_url = 'signin'
    def get(self, request):
        context={
            'user': request.user
        }
        return render(request,'profile.html')

class edit_profile(LoginRequiredMixin,View):
    login_url = 'signin'
    def get(self, request):
        context={
            'user': request.user
        }
        return render(request,'edit_profile.html',context)
    
    def post(self, request):
        form = Profile_edit_form(request.POST , request.FILES , instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        context={
            'user': request.user,
            'status': 'Oops! Something went wrong. Please try again.'
        }
        return render(request,'edit_profile.html',context)