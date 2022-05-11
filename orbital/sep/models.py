from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey

class User(AbstractUser):
    faculty = models.CharField(max_length=120)
    year = models.IntegerField(blank=True, null=True)
    major = models.CharField(max_length=120)
    sep = models.BooleanField(blank=True, null=True)
    pass

class Chat(models.Model):
    fromAddress = models.CharField(max_length=120)
    toAddress = models.CharField(max_length=120)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f'From: {self.fromAddress} To: {self.toAddress} Text: {self.text} Date: {str(self.date)}'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField(blank=True, null=True)
    period = models.TextField(blank=True, null=True)
    modules = models.TextField(blank=True, null=True)
    living = models.TextField(blank=True, null=True)
    prepare = models.TextField(blank=True, null=True)
    attachments = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'Reviewer: {self.user} University: {self.university} Date: {str(self.date)} Review: {self.review} Period: {self.period} Modules: {self.modules} Living: {self.living} Prepare: {self.prepare} Attachments: {self.attachments}'

# For site administrator
class Opening(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.text}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    opening = models.ForeignKey(Opening, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} placed {self.opening} on watchlist."

class PartnerUniversity(models.Model):
    forfaculty = models.CharField(max_length=120)
    puname = models.CharField(max_length=120)
    pumodule = models.CharField(max_length=120)
    pumodulecode = models.CharField(max_length=120)
    nusmodule = models.CharField(max_length=120)
    nusmodulecode = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.pumodulecode} in {self.puname} maps to {self.nusmodulecode} in NUS."