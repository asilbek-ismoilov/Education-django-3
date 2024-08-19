from django.db import models

class Instructors(models.Model):
    image = models.ImageField(upload_to='Images/instructors')
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.director}"

class Courses(models.Model):
    image = models.ImageField(upload_to='Images/courses')
    money = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    time = models.IntegerField()
    students = models.IntegerField()
    rating = models.IntegerField(default=0)  # Reyting uchun maydon

    def __str__(self):
        return f"{self.type} - {self.teacher}"

class Comments(models.Model):
    image = models.ImageField(upload_to='Images/students')
    name = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    message = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name} - {self.direction}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"