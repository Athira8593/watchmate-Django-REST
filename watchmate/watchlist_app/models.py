from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
        
    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=50)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.title
    
class Reviews(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    watch_list=models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return str(self.rating)+ "-" + self.watch_list.title