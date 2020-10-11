from django.shortcuts import render, redirect
from django.views import View
from watches.models import Brand
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
class IndexView(View):
    template_name = "main/index.html"
    
    def get(self, request, *args, **kwargs):
        print(request.user.is_superuser)
        brands = Brand.objects.all()
        context = { 'title': 'Home', 'scroll': True, 'brand_list': brands, 'comming_soon': range(4 - len(brands)), 'is_auth': request.user.is_authenticated }
        return render(request, self.template_name, context=context)

class LoginView(View):
    template_name = "main/login.html"
    
    def get(self, request, *args, **kwargs):
        context = { 'title': 'Login', 'scroll': False}
        return render(request, self.template_name, context=context)

    def post(self, request):
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('user-dashboard')
            return redirect('index')
        else:
            messages.error(request, 'Wrong Credentials')
            return redirect('login')

class WatchView(View):
    template_name = "main/watches.html"

    def get(self, request):
        pass

def Logout(request):
    logout(request)
    return redirect('login')