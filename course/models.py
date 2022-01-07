from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,
                             related_name='courses_user')
    title = models.CharField(max_length=200)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.title