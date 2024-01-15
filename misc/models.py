from django.db import models

class ReviewModel(models.Model):
    name=models.CharField(max_length=100)
    picture=models.URLField(max_length=200)
    email=models.EmailField(null=True,blank=True)
    review=models.TextField(null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
      
    def __str__(self):
        return f"{self.name} : {self.review}"