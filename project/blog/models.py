from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_content = models.TextField()
    post_image = models.ImageField()



    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})

