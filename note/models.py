from django.db import models
from django.urls import reverse
# Create your models here.

class Note(models.Model):

    title = models.CharField(max_length=50, verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заметки")

    IMP_STATUS = (
        ('v', 'Very important'),
        ('i', 'Important'),
        ('n', 'Not important')
    )

    importance = models.CharField(max_length=1, choices=IMP_STATUS, blank=True,default='n', help_text='Importance')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_page', kwargs={'pk': self.pk})