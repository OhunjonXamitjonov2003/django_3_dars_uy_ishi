from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=100,verbose_name='brand',unique=True)


    def __str__(self):
        return self.brand_name
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brendlar'
class Color(models.Model):
    color_name = models.CharField(max_length=80,verbose_name='rangi')


    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name = 'rang'
        verbose_name_plural = 'Ranglar'


class Car(models.Model):
    car_name = models.CharField(max_length=150,verbose_name='avtomabil nomi')

    role = models.CharField(max_length=50,blank=True,null=True,verbose_name='boshqaruvi')
    price = models.IntegerField(blank=True,null=True,verbose_name='narhi')
    created = models.DateTimeField(auto_now_add=True,verbose_name='kiritilgan vaqti')
    update = models.DateTimeField(auto_now=True,verbose_name='tahrirlangan vaqti')
    published = models.BooleanField(default=True,verbose_name='saytga chiqarish')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,verbose_name='brand nomi')
    color = models.ForeignKey(Color,on_delete=models.CASCADE,verbose_name='rangi')


    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = 'model'
        verbose_name_plural = 'Modellar'
        ordering = ('-pk',)