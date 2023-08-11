from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50)  # Change to CharField
    last_name = models.CharField(max_length=50)  # Change to CharField
    email = models.EmailField(max_length=100)  # Change to EmailField
    phone = models.CharField(max_length=15)  # Change to CharField
    address = models.CharField(max_length=100)  # Change to CharField
    city = models.CharField(max_length=50)  # Change to CharField
    state = models.CharField(max_length=50)  # Change to CharField
    zipcode = models.CharField(max_length=20)  # Change to CharField

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
