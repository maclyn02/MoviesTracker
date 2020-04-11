from django.shortcuts import render

# import class created in models.py
from .models import Movie

# Create your views here.
def home_page(request):
    # 'query' refers to 'name' input field in 'movies_stuff.html'
    user_query = str(request.GET.get('query',''))
    search_result = Movie.objects.filter(name__icontains = user_query)
    stuff_for_frontend = {"search_result" : search_result}

    return render(request,'movies/movies_stuff.html',stuff_for_frontend)
