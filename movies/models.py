from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

# imported in views.py
class Movie(models.Model):
    name = models.CharField(max_length=200)
    picture = models.URLField(max_length=500 , default='https://thefilmuniverse.com/wp-content/uploads/2019/09/Poster_Not_Available2.jpg')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    comments = models.TextField(max_length=2000 , default='')

    def __str__(self):
        return self.name
