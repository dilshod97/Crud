from django.db import models


class News(models.Model):
    title = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    describe = models.TextField()

    def __str__(self):
        return self.title