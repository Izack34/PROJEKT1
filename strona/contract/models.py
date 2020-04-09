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
    post = models.ForeignKey('blog.Post', on_delete=models.SET_NULL, null=True)
    # possible status: sent, resendedToC, resendedToE, applied, rejected, approved
    status = models.CharField(max_length=100)

    def __str__(self):
        return("Offer(" + self.client.get_username() + " -> " + self.executor.get_username() + ")")

class Contract(models.Model):
    status = models.CharField(max_length=100)
    offer = models.OneToOneField('Offer', on_delete=models.CASCADE)


class Request(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='applicant')
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return(self.applicant.get_username() + " -> " + self.post.title)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="sender")
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to")
    text = models.CharField(max_length=200)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    m_type = models.CharField(max_length=100)
    viewed = models.BooleanField(default=False)
