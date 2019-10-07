from django.db import models 

class Submission(models.Model):  
  artist_name = models.CharField(max_length=255)
  artwork_title = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  website = models.CharField(max_length=255)
  description = models.TextField(null=False) 
  category = models.CharField(max_length=255)

  def __str__(self):
        return self.artist_name