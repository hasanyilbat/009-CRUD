from django.urls import path
from .views import index
from .views import student_list
from .views import student_add
from .views import student_update
from .views import student_delete
from .views import student_detail
##!importları unutma

urlpatterns = [
 
    path("", index, name = "index"),
    path("list/", student_list , name="list"), ##!yeni bir pathte contexten veriyi çekip kullandık.
    path("add/", student_add, name="add"),
    path('update/<int:id>',student_update , name='update'),
    path('delete/<int:id>',student_delete , name='delete'),
    path('student/<int:id>', student_detail, name="detail"),
    
]