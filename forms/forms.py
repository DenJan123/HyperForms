from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=140, label='your name')
    age = forms.IntegerField(max_value=150, min_value=0, label='your age')
    favorite_book = forms.CharField(max_length=255, label='your favorite book')

# class DynamicForm(forms.Form):
#
#     def __init__(self, *args, **kwargs):
#         fields = kwargs.pop('fields')
#         for k,v in fields:
#

