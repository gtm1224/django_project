from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance,filename):
    return 'courses/user_{0}/{1}'.format(instance.user.id,filename)


class Course(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,
                             related_name='courses_user')
    title = models.CharField(max_length=200)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    video = models.FileField(blank=True,upload_to='videos/')
    attach = models.FileField(blank=True,upload_to=user_directory_path)


    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.title