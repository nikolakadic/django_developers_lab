from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.URLField(default='https://res.cloudinary.com/soundbetter/image/upload/c_fill,f_auto,g_face:auto,h_533,q_90,w_763/v1541355582/assets/photos/81936/DSC_5318_highcontrast.png')
    price = models.IntegerField(default=0)