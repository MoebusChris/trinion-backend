from django.db import models

from cores.general.utils.created_modified import createdModified  # type: ignore # noqa: I100


class Card(createdModified):

    creator = models.ForeignKey('users.User', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
