from django.db import models
from django.contrib.auth.models import User

class Offer(models.Model):
    price = models.FloatField()
    deadline = models.DateField()
    description = models.TextField()
    client = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='client')
    executor = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='executor')
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, null=True)


class Contract(models.Model):
    status = models.CharField(max_length=100)
    offer = models.OneToOneField('Offer', on_delete=models.CASCADE)


class Request(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='applicant')
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return(self.applicant.get_username() + " -> " + self.post.title) 
