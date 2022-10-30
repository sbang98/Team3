from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    imgfile = models.ImageField(null=True, upload_to="", blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    class Meta:
        db_table = 'Progress'
        verbose_name = 'Progress'
        verbose_name_plural = 'Progress'
