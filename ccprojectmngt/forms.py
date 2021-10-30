from django import forms

from document.models import (
   Project
)


ALPHABETIC_CHOICES = (
   ('---------', '---------'),
   ('a', 'A'),
   ('b', 'B'),
   ('c', 'C'),
)

class Filter(forms.Form):

   programa = forms.ChoiceField(
      choices=ALPHABETIC_CHOICES,
      widget=forms.Select(
         attrs={
            'class': 'form-control'}))
   
   consultora = forms.ModelChoiceField(
      queryset=Project.objects.values('programa','consultora','nombre_solicitante'),
      widget=forms.Select(
         attrs={
            'class': 'form-control'}))
   
   nombre_solicitante = forms.ModelChoiceField(
      queryset=Project.objects.values('programa','consultora','nombre_solicitante'),
      widget=forms.Select(
         attrs={
            'class': 'form-control'}))
   
