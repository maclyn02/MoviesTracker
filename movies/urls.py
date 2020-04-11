from django.urls import path
<<<<<<< HEAD
from .views import home_page, create, edit, delete


urlpatterns = [
    path('', home_page, name='home_page'),
    path('create/', create, name='create'),
    path('edit/<str:movie_id>', edit, name='edit'),
    path('delete/<str:movie_id>', delete, name='delete')
=======
from .views import home_page

urlpatterns = [
    path('', home_page , name = 'home_page')
>>>>>>> step_0_start
]
