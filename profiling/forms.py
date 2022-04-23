from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.forms import DateInput


from .models import Profile

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""


    username = UsernameField(widget=forms.TextInput(
        attrs={ 'class': 'form-control input-transparent pl-3', 'placeholder': 'Username', 'id': 'username', 'required': 'true'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control input-transparent pl-3',
            'placeholder': 'Password',
            'id': 'password',
            'required': 'true'
        }
    ))

class profile_form(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name',
                  'middle_name',
                  'last_name',
                  'suffix',
                  'region',
                  'province',
                  'municipality',
                  'barangay',
                  'purok',
                  'sex',
                  'age',
                  'birthday',
                  'email',
                  'contact_number',
                  'civil_status',
                  'youth_classification',
                  'youth_age_group',
                  'work_status',
                  'educational_background',
                  'sk_voter',
                  'national_voter'

                  
                  
                  
                  ]
        labels = {
            'first_name':'',
            'middle_name':'',
            'last_name':'',
            'suffix':'',
            'region':'',
            'province':'',
            'municipality':'',
            'barangay':'',
            'purok':'',
            'sex':'',
            'age':'',
            'birthday':'',
            'email':'',
            'contact_number':'',
            'civil_status':'',
            'youth_classification':'',
            'youth_age_group':'',
            'work_status':'',
            'educational_background':'',
            'sk_voter':'',
            'national_voter':''
             }
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}),
            
        }
    def __init__(self, *args, **kwargs):
        super(profile_form, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['middle_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['suffix'].widget.attrs['class'] = 'form-control'
        self.fields['region'].widget.attrs['class'] = 'form-control'
        self.fields['province'].widget.attrs['class'] = 'form-control'
        self.fields['municipality'].widget.attrs['class'] = 'form-control'
        self.fields['barangay'].widget.attrs['class'] = 'form-control'
        self.fields['purok'].widget.attrs['class'] = 'form-control'
        self.fields['sex'].widget.attrs['class'] = 'form-control'
        self.fields['age'].widget.attrs['class'] = 'form-control'
        self.fields['birthday'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['contact_number'].widget.attrs['class'] = 'form-control'
        self.fields['civil_status'].widget.attrs['class'] = 'form-control'
        self.fields['youth_classification'].widget.attrs['class'] = 'form-control'
        self.fields['youth_age_group'].widget.attrs['class'] = 'form-control'
        self.fields['work_status'].widget.attrs['class'] = 'form-control'
        self.fields['educational_background'].widget.attrs['class'] = 'form-control'
        self.fields['sk_voter'].widget.attrs['class'] = 'form-control'
        self.fields['national_voter'].widget.attrs['class'] = 'form-control'
        
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['middle_name'].widget.attrs['placeholder'] = 'Middle Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['suffix'].widget.attrs['placeholder'] = 'Suffix'
        self.fields['region'].widget.attrs['placeholder'] = 'Region'
        self.fields['province'].widget.attrs['placeholder'] = 'Province'
        self.fields['municipality'].widget.attrs['placeholder'] = 'Municipality'
        self.fields['barangay'].widget.attrs['placeholder'] = 'Barangay'
        self.fields['purok'].widget.attrs['placeholder'] = 'Purok'
        self.fields['sex'].widget.attrs['placeholder'] = 'Sex'
        self.fields['age'].widget.attrs['placeholder'] = 'Age'
        self.fields['birthday'].widget.attrs['placeholder'] = 'Birthday'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['contact_number'].widget.attrs['placeholder'] = 'Contact Number'
        self.fields['civil_status'].widget.attrs['placeholder'] = 'Civil Status'
        self.fields['youth_classification'].widget.attrs['placeholder'] = 'Youth Classification'
        self.fields['youth_age_group'].widget.attrs['placeholder'] = 'Youth Age Group'
        self.fields['work_status'].widget.attrs['placeholder'] = 'Work Status'
        self.fields['educational_background'].widget.attrs['placeholder'] = 'Educational Background'
        self.fields['sk_voter'].widget.attrs['placeholder'] = 'SK Voter'
        self.fields['national_voter'].widget.attrs['placeholder'] = 'National Voter'

        
    # def clean(self):
    #     super(profile_form, self).clean()
    #     first_name = self.cleaned_data['first_name']
    #     last_name = self.cleaned_data['last_name']
    #     if self.cleaned_data['middle_name'] != "":
    #         middle_name = self.cleaned_data['middle_name']
    #         if Profile.objects.filter(first_name=first_name, middle_name=middle_name,last_name=last_name).exists():
    #             raise forms.ValidationError(f'"{first_name, middle_name, last_name}" already exists')
    #         return first_name
    #     else:
    #         if Profile.objects.filter(first_name=first_name, last_name=last_name).exists():
    #             raise forms.ValidationError(f'"{first_name,last_name}" already exists')
    #         return first_name