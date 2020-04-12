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
            print("Error in  Create " + e)
            pass

    return redirect('/')

#'movieID' is passed explicitly from frontend -> form action(also in urls.py path[])
def edit(request , movieID):
    if request.method == 'POST':
        data = {
            'name' : request.POST.get('edit-movie_name'),
            'picture' : request.POST.get('edit-movie_picture'),
            'rating' : int(request.POST.get('edit-movie_rating')),
            'comments' : request.POST.get('edit-movie_comments')
        }
        try:
            movieObj = Movie.objects.get(id=movieID)
            movieObj.name = data.get('name')
            movieObj.picture = data.get('picture')
            movieObj.rating = int(data.get('rating'))
            movieObj.comments = data.get('comments')

            movieObj.save()

        except Exception as e:
            print("Error in  Edit " + e)
            pass

    return redirect('/')

def delete(request , movieID):
    try:
        movieObj = Movie.objects.get(id=movieID)
        movieObj.delete()

    except Exception as e:
        print("Error in  Delete " + e)
        pass

    return redirect('/')
