from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import CustomUser
from .forms import CustomUserCreateForm, CustomUserUpdateForm

# Create your views here.
class UserRegisterView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "users/users_create.html"
    login_url = '/login/'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        context = { 'title': 'User Register' }
        return render(request, self.template_name, context)

    def post(self, request):
        context = { 'title': 'User Register' }
        form = CustomUserCreateForm(request.POST, request.FILES) # request.FILES to get the uploaded picture
        non_required_fields = (
            'middle_name', 
            'height', 
            'weight', 
            'religion',
            'mother_name',
            'mother_occupation',
            'father_name',
            'father_occupation',
            'spouse_name',
            'spouse_occupation',
        )
        if form.is_valid():
            user = form.save(commit=False)

            # If some non-required fields has data
            for field in non_required_fields:
                data = request.POST.get(field)
                user.__dict__[field] = data if data != '' else None
            user.zip_code = int(request.POST.get('zip_code')) if request.POST.get('zip_code') != '' else None
            user.profile = request.FILES.get('profile') if request.FILES.get('profile') is not None else 'profile/profile_default.png'
            user.save()
            return redirect('user-dashboard')
        else:
            context['errors'] = form.error_messages
            print(type(form.errors))
            print(form.errors)            
            return render(request, self.template_name, context)

class UserDashboardView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "users/users_read_all.html"
    login_url = '/login/'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        users = CustomUser.objects.filter(is_superuser=False)
        context = { 'title': 'User Dashboard', 'user_list': users, 'url_add': 'user-register' }
        return render(request, self.template_name, context)

    def post(self, request):
        id = request.POST.get('object_id')
        custom_user = get_object_or_404(CustomUser, id=id)
        custom_user.delete()
        return redirect('user-dashboard')
        
class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "users/users_update.html"
    login_url = '/login/'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, user_id):
        user = CustomUser.objects.get(id=user_id)

        context = { 'title': 'User Update', 'user': user }
        return render(request, self.template_name, context)

    def post(self, request, user_id):
        custom_user = get_object_or_404(CustomUser, id=user_id)
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=custom_user)

        non_required_fields = (
            'middle_name', 
            'height', 
            'weight', 
            'religion',
            'mother_name',
            'mother_occupation',
            'father_name',
            'father_occupation',
            'spouse_name',
            'spouse_occupation',
        )
        if form.is_valid():
            user = form.save(commit=False)

            # If some non-required fields has data
            for field in non_required_fields:
                data = request.POST.get(field)
                user.__dict__[field] = data if data != '' else None
            user.zip_code = int(request.POST.get('zip_code')) if request.POST.get('zip_code') != '' else None
            user.profile = request.FILES.get('profile') if request.FILES.get('profile') is not None else 'profile/profile_default.png'
            if request.POST.get('password1') != '' and request.POST.get('password1') != '' and request.POST.get('password1') == request.POST.get('password2'):
                user.set_password(request.POST.get('password1'))
            user.save()
            return redirect('user-dashboard')
        else:
            # context['errors'] = form.error_messages
            print(type(form.errors))
            print(form.errors)            
            return redirect('user-update', user_id)

