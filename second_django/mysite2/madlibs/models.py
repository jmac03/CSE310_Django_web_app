from django.db import models

# A class to hold one story and many word choices
class Master(models.Model):
    master_text = models.CharField(max_length=200)
    story_name = models.CharField(max_length=200)

    def __str__(self):
        return self.master_text

# A class to create text entry fields
class TextEntry(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    entry_text = models.CharField(max_length=200)
    phonics = models.CharField(max_length=200)

    def __str__(self):
        return self.entry_text