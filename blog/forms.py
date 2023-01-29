from django import forms
 
# creating a form

class SequenceForm(forms.Form):
    x_sequence = forms.CharField(label='x_sequence', max_length=1000)
    y_sequence = forms.CharField(label='y_sequence', max_length=1000)
    degree = forms.IntegerField(label='degree', min_value=1, max_value=5)