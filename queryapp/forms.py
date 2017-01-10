from queryapp.models import *
from django import forms
class loginForm(forms.ModelForm):                       
	id1 = forms.IntegerField(label='Id')              
	uname = forms.CharField(label='Username')      
	pwd = forms.CharField(label='Password')         
                
	class Meta:                           
		model = loginInfo                         
		fields = '__all__'   

class studentForm(forms.ModelForm):
	class Meta:
		model = student
		fields = '__all__'

class questionForm(forms.ModelForm):
	class Meta:
		model=question
		fields='__all__'

class answerForm(forms.ModelForm):
	class Meta:
		model=answer
		fields='__all__'