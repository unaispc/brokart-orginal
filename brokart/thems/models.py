from django.db import models

# MODEL FOR THEMS
class SiteSetting(models.Model):
    banner=models.ImageField(upload_to='media/site')
    caption=models.TextField()
