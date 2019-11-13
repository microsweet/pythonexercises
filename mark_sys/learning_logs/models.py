from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Mate:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."
