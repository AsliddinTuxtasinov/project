from django.db import models
from django.urls import reverse


class Catagory(models.Model):
    catagory = models.CharField(max_length=50)
    slug_catagory = models.SlugField(default = "", null=False, db_index=True) # kiyinchalik foydalaniladi

    def __str__(self):
        return self.catagory
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name="catagoriyalar")
    describetion = models.TextField()
    image = models.ImageField(upload_to="post_image")
    slug_post = models.SlugField(default = "", null=False, db_index=True)

    def get_url(self):
        return reverse("post", args = [self.slug_post])

    def __str__(self):
        return self.title