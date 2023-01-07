from django.contrib import admin

from .models import Gallery, Picture
from PIL import  Image
from .forms import PictureAdminForm

class GalleryAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Gallery, GalleryAdmin)

class PictureAdmin(admin.ModelAdmin):
    form = PictureAdminForm
    def save_model(self, request, obj, form, change):

        obj.save()

        x = form.cleaned_data.get('x')
        y = form.cleaned_data.get('y')
        width = form.cleaned_data.get('width')
        height = form.cleaned_data.get('height')

        # Only crop image when x,y, width and height have been provided
        if x and y and width and height:
            image = Image.open(obj.image)
            cropped_image = image.crop((x,y,width + x, height + y))
            cropped_image.save(obj.image.path)

admin.site.register(Picture, PictureAdmin)