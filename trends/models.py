from django.db import models

# Create your models here.

class Trend(models.Model):
    year = models.CharField(max_length=5)
    idea = models.CharField(max_length=100)
    level = models.IntegerField()
    def __str__(self):
        return self.idea
    
class TrendNews(models.Model):
    text = models.TextField()
    from_user = models.CharField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.from_user}:{self.date}"