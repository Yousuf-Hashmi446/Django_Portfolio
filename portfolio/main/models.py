from django.db import models

# Create your models here.

class Header(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    title_line = models.CharField(max_length=100)


class AboutMe(models.Model):
    paragraph = models.TextField()


class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year = models.IntegerField()


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name  # Display name in admin panel
