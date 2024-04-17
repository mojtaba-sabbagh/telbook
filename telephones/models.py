from django.db import models
from django.contrib.auth.models import User

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
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ['last_name']
        verbose_name = "مشخصات کاربر"
        verbose_name_plural = "مشخصات کاربران"

class Department(models.Model):
    TITLE_CHOICES = (
        ('معاونت', 'معاونت'),
        ('مدیریت', 'مدیریت'),
        ('دانشکده', 'دانشکده'),
        ('گروه', 'گروه'),
        ('اداره', 'اداره'),
        ('دبیرخانه', 'دبیرخانه'),
        ('حوزه', 'حوزه'),
        ('مرکز', 'مرکز'),
        ('کمیته', 'کمیته'),
        ('شورا', 'شورا'),
        ('سرای', 'سرای دانشجوی'),
        ('گیت', 'گیت'),
    )
    dep_title = models.CharField(max_length=255, blank=True, null=True, choices=TITLE_CHOICES)
    dep_name = models.CharField(max_length=255)
    dep_address = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(default=0)
    super_dep = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name="the related dep")

    def __str__(self):
        return f"{self.dep_title} {self.dep_name}"

    class Meta:
        ordering = ['dep_title', 'dep_name']
        verbose_name = "واحد سازمانی"
        verbose_name_plural = "واحدهای سازمانی"

class Telephone(models.Model):
    extension = models.CharField(max_length=255, unique=True)
    complete_number = models.CharField(max_length=255, blank=True, null=True)
    tel_address = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.extension}"

    class Meta:
        ordering = ['extension']
        verbose_name = "تلفن داخلی"
        verbose_name_plural = "تلفن‌های داخلی"

class PositionType(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    level = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['title']
        verbose_name = "نوع پست سازمانی"
        verbose_name_plural = "انواع پست های سازمانی"

class Position(models.Model):
    position_type =  models.ForeignKey(PositionType, related_name='position_types', on_delete=models.CASCADE, verbose_name="the related position type")
    dep = models.ForeignKey(Department, related_name='deps', on_delete=models.CASCADE, verbose_name="the related dep")
    owner = models.ForeignKey(Profile, related_name='owners', on_delete=models.CASCADE, verbose_name="the related profile")
    duties = models.CharField(max_length=255, blank=True, null=True, default='')

    def __str__(self):
        return f"{self.position_type} {self.dep.dep_name} - {self.owner}"

    class Meta:
        ordering = ['dep', 'position_type', 'owner']
        verbose_name = "پست سازمانی"
        verbose_name_plural = "پست‌های سازمانی"

class Assign(models.Model):
    date = models.DateField(blank=True, null=True)
    position = models.ForeignKey(Position, related_name='positions', on_delete=models.CASCADE, verbose_name="the related pos")
    tel = models.ForeignKey(Telephone, related_name='tels', on_delete=models.CASCADE, verbose_name="the related tel")


    def __str__(self):
        return f"{self.tel} - {self.position}"

    class Meta:
        ordering = ['tel']
        verbose_name = "تخصیص تلفن"
        verbose_name_plural = "تخصیص تلفن‌ها"

