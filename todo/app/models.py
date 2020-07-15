from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(default="")
    status = models.IntegerField(default=0)

    def __str__(self):
        if self.status == 0:
            status = "TODO"
        elif self.status == 1:
            status = "In-Progress"
        return self.title + " " + self.status