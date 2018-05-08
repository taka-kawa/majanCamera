from django.db import models


class PisImage(models.Model):
    image = models.ImageField(upload_to='api')