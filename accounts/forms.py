from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class DateInput(forms.DateInput):
    input_type = 'date'


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = (
            'name', 'Mobile_no', 'land_ha', 'soil_ph', 'soil_type', 'district', 'location', 'category', 'currentCrop',
            'prevCrop', 'user','datOfSow',
            'yield_tons','ElecConduc','OrgCarbonP','Nitrogenkgha','Phosphoruskgha','Potassium_kgha','Sulphur_ppm','Zinc_ppm','Boron_ppm','Ironppm','Manganese_ppm','Copper_ppm','Waterph'
        )
        widgets = {'datOfSow':DateInput(),
'user': forms.HiddenInput()}


class sms_crop_form(forms.ModelForm):
    class Meta:
        fields = ('user', 'crop')
        widgets = {'user': forms.HiddenInput()}


class NoCurForm(forms.ModelForm):
    class Meta:
        model=Subscriber
        fields =(
            'name', 'Mobile_no', 'land_ha', 'soil_ph', 'soil_type', 'district', 'location', 'category',
            'prevCrop', 'user',
            'yield_tons',
            'ElecConduc', 'OrgCarbonP', 'Nitrogenkgha', 'Phosphoruskgha', 'Potassium_kgha', 'Sulphur_ppm', 'Zinc_ppm', 'Boron_ppm', 'Ironppm', 'Manganese_ppm', 'Copper_ppm', 'Waterph'
        )
        widgets = {'user': forms.HiddenInput()}
