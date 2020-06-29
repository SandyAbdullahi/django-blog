from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.TextField(blank=True)
    post_image = models.ImageField(blank=True)

    @property
    def get_photo_url(self):
        if self.post_image and hasattr(self.post_image, 'url'):
            return self.post_image.url
        else:
            return "unavailable"

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})

