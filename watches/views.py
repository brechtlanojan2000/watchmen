from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Watch, Brand, WatchImage
from .forms import WatchForm, BrandForm, WatchImageForm

# Create your views here.
class WatchRegisterView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "watches/watches_create.html"
    login_url = '/login/'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        brand = Brand.objects.all()
        context = { 'title': 'Watch Register', 'brand_list': brand, 'num_images': range(4) }
        return render(request, self.template_name, context)

    def post(self, request):
        form = WatchForm(request.POST, request.FILES)

        if form.is_valid():
            watch = form.save()
            optional_images = ('imageOptional0', 'imageOptional1', 'imageOptional2', 'imageOptional3')
            for image in optional_images:
                if request.FILES.get(image) is not None:
                    WatchImage(watch=watch, image=request.FILES.get(image)).save()
            return redirect('watch-dashboard')
        else:
            return redirect('watch-register')

class WatchDashboardView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "watches/watches_read_all.html"
    login_url = '/login/'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        watch = Watch.objects.all()
        context = { 'title': 'Watch Dashboard', 'watch_list': watch, 'url_add': 'watch-register' }
        return render(request, self.template_name, context)

    def post(self, request):
        id = request.POST.get('object_id')
        watch = get_object_or_404(Watch, id=id)
        watch.delete()
        return redirect('watch-dashboard')

class WatchUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "watches/watches_update.html"
    login_url = '/login/'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, watch_id):
        brand = Brand.objects.all()
        watch = Watch.objects.get(id=watch_id)
        watch_images = WatchImage.objects.filter(watch=watch)
        context = { 'title': 'Watch Update', 'brand_list': brand, 'watch': watch, 'num_images': range(len(watch_images), 4), 'watch_image_list': watch_images }
        return render(request, self.template_name, context)

    def post(self, request, watch_id):
        watch = get_object_or_404(Watch, id=watch_id)
        form = WatchForm(request.POST, request.FILES, instance=watch)

        if form.is_valid():
            watch = form.save()
            optional_images = ('imageOptional0', 'imageOptional1', 'imageOptional2', 'imageOptional3')
            for image in optional_images:
                if request.FILES.get(image) is not None:
                    WatchImage(watch=watch, image=request.FILES.get(image)).save()
            return redirect('watch-dashboard')
        else:
            return redirect('watch-update')

class BrandRegisterView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "brands/brands_create.html"
    login_url = '/login/'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        context = { 'title': 'Brand Register' }
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = { 'title': 'Brand Register' }
        form = BrandForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('brand-dashboard')
        else:
            return redirect('brand-register')

class BrandDashboardView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "brands/brands_read_all.html"
    login_url = '/login/'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        brand = Brand.objects.all()
        context = { 'title': 'Brand Dashboard', 'brand_list': brand, 'url_add': 'brand-register' }
        return render(request, self.template_name, context)

    def post(self, request):
        id = request.POST.get('object_id')
        type_of_form = request.POST.get('type_of_form')
        brand = get_object_or_404(Brand, id=id)

        if type_of_form == 'update':
            form = BrandForm(request.POST, request.FILES, instance=brand)
            if form.is_valid():
                form.save()
        else:
            brand.delete()
        return redirect('brand-dashboard')

        
    
