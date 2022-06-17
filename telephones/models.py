from django.db import models
from django.contrib.auth.models import User
from matplotlib.pyplot import title

# Create your models here.

class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'مرد'),
        ('F', 'زن'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, default='M', choices=GENDER_CHOICES)
    birthday = models.DateField(blank=True, null=True)
    national_id = models.CharField(max_length=10, unique=True, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name']

class Department(models.Model):
    TITLE_CHOICES = (
        ('معاونت', 'معاونت'),
        ('مدیریت', 'مدیریت'),
        ('گروه', 'گروه'),
        ('اداره', 'اداره'),
        ('دبیرخانه', 'دبیرخانه'),
        ('حوزه', 'حوزه'),
        ('مرکز', 'مرکز'),
        ('کمیته', 'کمیته'),
    )
    dep_title = models.CharField(max_length=255, blank=True, null=True, choices=TITLE_CHOICES)
    dep_name = models.CharField(max_length=255)
    dep_address = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(default=0)
    super_dep = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name="the related dep")

    def __str__(self):
        return f"{self.dep_title} {self.dep_name}"

    class Meta:
        ordering = ['dep_name']

class Telephone(models.Model):
    extension = models.CharField(max_length=255)
    complete_number = models.CharField(max_length=255, blank=True, null=True)
    tel_address = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.extension}"

    class Meta:
        ordering = ['extension']

class PositionType(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    level = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['title']


class Position(models.Model):
    position_type =  models.ForeignKey(PositionType, on_delete=models.CASCADE, verbose_name="the related position type")
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="the related profile")
    dep = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="the related dep")

    def __str__(self):
        return f"{self.position_type} {self.dep.dep_name} - {self.owner}"

    class Meta:
        ordering = ['position_type']

class Assign(models.Model):
    date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="the related profile")
    dep = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="the related pos")
    tel = models.ForeignKey(Telephone, on_delete=models.CASCADE, verbose_name="the related tel")


    def __str__(self):
        return f"{self.tel} - {self.owner}"

    class Meta:
        ordering = ['tel']

