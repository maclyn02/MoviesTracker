from django.shortcuts import render, redirect
from django.contrib import messages

# import class created in models.py
from .models import Movie

# Create your views here.
def home_page(request):
    # 'query' refers to 'name' input field in 'movies_stuff.html'
    user_query = str(request.GET.get('query',''))
    search_result = Movie.objects.filter(name__icontains = user_query)
    stuff_for_frontend = {
                            "search_result" : search_result,
                            "no_of_records" : len(search_result)
                            }
    print(stuff_for_frontend["no_of_records"])
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

            messages.success(request, "Added new Drama : {}".format(data.get('name')))
        except Exception as e:
            messages.warning(request, "Error creating new entry {}".format(e))

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
            messages.success(request, "Updated 1 Drama : {}".format(data.get('name')))

        except Exception as e:
            messages.warning(request, "Error in updating {}".format(e))

    return redirect('/')

def delete(request , movieID):
    try:
        movieObj = Movie.objects.get(id=movieID)
        movie_name = movieObj.name;
        movieObj.delete()
        messages.success(request, f"Deleted 1 Drama : {movie_name}")

    except Exception as e:
        messages.warning(request, "Error in delete {}".format(e))

    return redirect('/')
