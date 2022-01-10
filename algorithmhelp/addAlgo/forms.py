from django import forms
from .models import addAlgorithm

class addAlgorithmForm(forms.ModelForm):    
    class Meta:
        model = addAlgorithm
        
        fields = ("name", "timeComplexity", "spaceComplexity", "description", "applications", "implementation", "output")