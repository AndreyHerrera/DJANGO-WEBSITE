from django.db import models

class ToDoList(models.Model):
    author = models.CharField(max_length = 50)
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 256)

    def __str__(self) -> str:
        return '{}'.format(self.title)

    class Meta:
        db_table = 'ToDoList'
    