from django import forms

from users.models import CustomUser, MedicalProductCategory, MedicalProduct


class SignInForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class ShopEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'address', 'phone_number', 'image', 'city', 'state', 'country']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = MedicalProductCategory
        fields = ['name', 'description']


class MedicalProductForm(forms.ModelForm):
    class Meta:
        model = MedicalProduct
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control select2'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shop'].queryset = CustomUser.objects.filter(role='shop')
        self.fields['image'].widget.attrs.update({'class': 'form-control-file', 'accept': 'image/*'})


class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'image']


class ShopUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'image', 'address', 'city', 'state',
                  'country']
