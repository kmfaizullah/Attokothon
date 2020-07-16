from django import forms
from .models import Signup,blog,bestPlace,memory, todo

"""
    These classes is to insert the values into the database.
    Django form has been used here.
    Labels dictionary has been used to change the model filed name.

"""

# this is for signup
class SignupForm(forms.ModelForm):

    class Meta:
        model = Signup
        fields = ('first_name','last_name','user_name','password','mobile')
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'user_name':'User Name',
            'password':'Password',
            'mobile':'Mobile',
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm,self).__init__(*args, **kwargs)

        self.fields['mobile'].required = False

# this is for inserting blog post
class blogForm(forms.ModelForm):

    class Meta:
        model = blog
        fields = ('title','post','date')
        labels = {
            'title':'Title',
            'post':'Post',
            'date':'Date'
        }

    def __init__(self, *args, **kwargs):
        super(blogForm,self).__init__(*args, **kwargs)
        
        self.fields['date'].required = False

# this is for inserting best place
class bestPlaceForm(forms.ModelForm):

    class Meta:
        model = bestPlace
        fields = ('title','post','date','keypoints')
        labels = {
            'title':'Title',
            'post':'Post',
            'date':'Date',
            'keypoints': 'Key Points'
        }

    def __init__(self, *args, **kwargs):
        super(bestPlaceForm,self).__init__(*args, **kwargs)
        
        self.fields['date'].required = False

# this is for inserting memorable place data
class memoryForm(forms.ModelForm):

    class Meta:
        model = memory
        fields = ('title','post','date','note')
        labels = {
            'title':'Title',
            'post':'Post',
            'date':'Date',
            'note': 'Note'
        }

    def __init__(self, *args, **kwargs):
        super(memoryForm,self).__init__(*args, **kwargs)
        
        self.fields['date'].required = False


# this one is for inserting todo table data
class todoForm(forms.ModelForm):

    class Meta:
        model = todo
        fields = ('task','place','date','note')
        labels = {
            'task':'Task',
            'place':'Place',
            'date':'Date',
            'note': 'Note'
        }

    def __init__(self, *args, **kwargs):
        super(todoForm,self).__init__(*args, **kwargs)
