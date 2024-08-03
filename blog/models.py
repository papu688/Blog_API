from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title
