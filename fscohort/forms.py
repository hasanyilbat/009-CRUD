from django import forms
from .models import Student



#! /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
#! /*/                                     /*/
#! /*/         CRUD  - CREATE (POST)       /*/
#! /*/                                     /*/
#! /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/



#! verileri form yapısıyla göndericez.
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__' 
        labels = {"first_name": "Adınız", "last_name":"Soyadınız", "number":"Numaranız"}