from django.db import models

# Create your models here.

class TextField(models.Model):
    entry_text = models.CharField(max_length=200)

    def __str__(self):
        return self.entry_text