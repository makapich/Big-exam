from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'


class Logs(models.Model):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    METHOD_CHOICES = [
        (GET, 'GET'),
        (POST, 'POST'),
        (PUT, 'PUT'),
        (DELETE, 'DELETE'),
    ]

    path = models.CharField(max_length=255)
    method = models.CharField(max_length=6, choices=METHOD_CHOICES, default=GET)
    timestamp = models.DateTimeField(auto_now_add=True)
    get_data = models.JSONField(blank=True, null=True)
    post_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.timestamp}, {self.method}'

    class Meta:
        verbose_name_plural = 'Logs'
