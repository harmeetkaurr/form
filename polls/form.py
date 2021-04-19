from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import college_form, student_form, login

class College_Form(forms.ModelForm):
    class Meta:
        model = college_form
        fields = ('first_name',
                  'last_name',
                  'father_name',
                  'mother_name',
                  'email',
                  'mobile',
                  'course',
                  )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'father_name',
            'mother_name',
            'email',
            'mobile',
            'course',
             Submit('submit', 'Submit', css_class='btn btn-success'),
        )



class StuDent_Form(forms.ModelForm):
    class Meta:
        model = student_form
        fields = ('first_name',
                  'last_name',
                  'father_name',
                  'mother_name',
                  'email',
                  'mobile',
                  'classes',
                  )


    def __init__(self, *args, **kwards):
        super().__init__(*args, **kwards)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'father_name',
            'mother_name',
            'mobile',
            'email',
            'classes',
            Submit('submit', 'Submit', css_class='btn btn-success')
        )


class Login(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    retype_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = login
        fields = ('email',
                  'password',
                  'retype_password',
                  )


    def __init__(self, *args, **kwards):
        super().__init__(*args, **kwards)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'email',
            'password',
            'retype_password',
            Submit('submit', 'Submit', css_class='btn btn-success')
        )



