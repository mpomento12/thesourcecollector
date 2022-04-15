from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
LISTEN = (
    ('M', 'Melvin'),
    ('I', 'Info'),
    ('O', 'Osario')
)

class Format(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('formats_detail', kwargs={'pk': self.id})

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    release = models.IntegerField()
    formats = models.ManyToManyField(Format)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'album_id': self.id})

class Listening(models.Model):
    date = models.DateField('listening date')
    listen = models.CharField(
        max_length=1,
        choices=LISTEN,
        default=LISTEN[0][0]
        )
    
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_listen_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']