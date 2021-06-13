from django.urls import path
from .views import Board , Comment

app_name =  'board'
urlpatterns = [
     
    path('' , Board , name='commentboard'),
    path('comment/',Comment, name='comment'),
    

]