from django.db import models

# Create your models here.


class Record(models.Model):
    created_date=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zipcode=models.IntegerField()


    def __str__(self):
        return (f'{self.first_name}, {self.last_name}')