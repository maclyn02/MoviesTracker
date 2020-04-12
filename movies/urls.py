from django.urls import path
from .views import home_page
from .views import create
from .views import edit
from .views import delete

urlpatterns = [
#parameter 1 refers to actual url pattern
#parameter 2 refers to function name in views
#paramater 'name' should match call in form action
    path('', home_page , name = 'home_page'),
    path('create/' , create , name='create'),
    path('edit/<str:movieID>' , edit , name='edit'),
    path('delete/<str:movieID>' , delete , name='delete')
]
