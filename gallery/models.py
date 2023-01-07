from django.db import models

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

class Picture(models.Model):
    image = models.ImageField(upload_to='pictures')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='pictures')

    def __str__(self):
        return self.image.name

