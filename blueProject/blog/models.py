from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]