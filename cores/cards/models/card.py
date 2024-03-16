from django.db import models

from cores.general.utils.created_modified import createdModified



class Card(createdModified):
    
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    asignee = models.ManyToManyField('users.User', blank=True)

    def __str__(self):
        return self.title
