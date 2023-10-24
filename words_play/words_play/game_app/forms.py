#game_app
from django import forms

class LetterForm(forms.Form):
    letter = forms.CharField()
    number = forms.IntegerField(
        label = "Select Number",
        min_value = 1,
        max_value =10
        )
    # Add more fields as needed
