from django import forms
from app_shop.models import UserProfile

class ContactForm(forms.Form):
    name = forms.CharField(label="Họ tên: ", max_length=200, widget=forms.TextInput(attrs={
        "class":"form-control bg-light border-0 px-4",
        "placeholder":"Họ tên",
        "style":"height: 55px;"
    }))
    email = forms.EmailField(label="Email: ", widget=forms.EmailInput(attrs={
        "class":"form-control bg-light border-0 px-4",
        "placeholder":"Email",
        "style":"height: 55px;"
    }))
    subject = forms.CharField(label="Tiêu đề: ", max_length=250, widget=forms.TextInput(attrs={
        "class":"form-control bg-light border-0 px-4",
        "placeholder":"Tiêu đề",
        "style":"height: 55px;"
    }))
    message = forms.CharField(label="Nội dung: ", widget=forms.Textarea(attrs={
        "class":"form-control bg-light border-0 px-4 py-3",
        "placeholder":"Nội dung",
        "rows":"4"
    }))

# class UserProfileForm(forms.ModelForm):
#     name = forms.CharField(label='Họ tên', widget=forms.TextInput(attrs={
#         "class":"form-control bg-light border-0 px-4",
#         "placeholder":"Họ tên",
#         "style":"height: 55px;"
#     }))
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
#         "class":"form-control bg-light border-0 px-4",
#         "placeholder":"Email",
#         "style":"height: 55px;"
#     }))
#     password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(attrs={
#         "class":"form-control bg-light border-0 px-4",
#         "placeholder":"Mật khẩu",
#         "style":"height: 55px;"
#     }))
#     avatar = forms.ImageField(label='Hình đại diện', required=False, widget=forms.FileInput(attrs={
#         "class":"form-control",
#         "style":"height: 55px;"
#     }))

#     class Meta:
#         model = UserProfile
#         # fields = ['name','email','password', 'avatar']
#         fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # fields = ['name','email','password', 'avatar']
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                        "class": "form-control bg-light border-0 px-4",
                        "placeholder": "Họ tên",
                        "style": "height: 55px;"
                    }),
            'email': forms.EmailInput(attrs={
                        "class": "form-control bg-light border-0 px-4",
                        "placeholder": "Email",
                        "style": "height: 55px;"
                    }),
            'password': forms.PasswordInput(attrs={
                        "class": "form-control bg-light border-0 px-4",
                        "placeholder": "Mật khẩu",
                        "style": "height: 55px;"
                    }),
            'avatar': forms.FileInput(attrs={
                        "class": "form-control border-0 px-4",
                        "style": "height: 55px;"
                    })
        }
            
        labels = {
            'name': 'Họ tên',
            'email': 'Email',
            'password': 'Mật khẩu',
            'avatar': 'Hình đại diện',
        }