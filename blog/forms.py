from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Post, Category


choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category','text',)

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control'}),
            'category' : forms.Select(choices = choice_list, attrs = {'class':'form-control'})
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = "", widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label = "", max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label = "", max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category  # Replace with your actual model
        fields = ['name']  # Replace 'name' with the actual field name in your model

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label = "", max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label = "", max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Last Name'}))
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
    