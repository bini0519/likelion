from django.db import models

class Designer(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.name

    def summary(self):
        if len(self.description) >= 40:
            return self.description[:40] + str(" ...")
        else:
            return self.description
