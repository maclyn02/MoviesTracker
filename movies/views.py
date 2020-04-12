from django.shortcuts import render, redirect

# import class created in models.py
from .models import Movie

# Create your views here.
def home_page(request):
    # 'query' refers to 'name' input field in 'movies_stuff.html'
    user_query = str(request.GET.get('query',''))
    search_result = Movie.objects.filter(name__icontains = user_query)
    stuff_for_frontend = {"search_result" : search_result}

    return render(request,'movies/movies_stuff.html',stuff_for_frontend)

def create(request):
    # import pdb
    # pdb.set_trace()
    if request.method == 'POST':
        data = {
            'name' : request.POST.get('movie_name'),
            'picture' : request.POST.get('movie_picture'),
            'rating' : int(request.POST.get('movie_rating')),
            'comments' : request.POST.get('movie_comments')
        }
        try:
            response = Movie.objects.create(
                name = data.get('name'),
                picture = data.get('picture'),
                rating = data.get('rating'),
                comments = data.get('comments')
            )
        except Exception as e:
            print(e)
            pass

    return redirect('/')
