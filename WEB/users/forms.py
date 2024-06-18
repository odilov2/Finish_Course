from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

    # def save(self, commit=True):
    #     user = super().save(commit)
    #     user.set_password(self.cleaned_data['password'])
    #     user.save()
    #     return user



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)