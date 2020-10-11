from django.forms import ModelForm
from .models import Watch, Brand, WatchImage

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        exclude = ('date_created',)

class WatchForm(ModelForm):
    class Meta:
        model = Watch
        exclude = ('date_created',)

class WatchImageForm(ModelForm):
    class Meta:
        model = WatchImage
        fields = ('__all__')