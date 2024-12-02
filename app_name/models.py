from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)  
    release_year = models.IntegerField()     
    genre = models.CharField(max_length=50)  

    def __str__(self):
        return self.title  

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')  
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    content = models.TextField()  
    rating = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'Review for {self.movie.title} by {self.user.username}'
