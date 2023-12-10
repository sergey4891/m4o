from django.db import models


class Persons(models.Model):
    class Gender(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField(auto_now_add=True)
    # photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
    #                           blank=True, null=True, verbose_name="Фото")
    phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    last_job = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Partner(models.Model):
    name_legal_entity = models.CharField(max_length=255)
    ogrn = models.IntegerField(max_length=15)
    legal_address = models.CharField(max_length=255)
    inn = models.IntegerField(max_length=12)
    kpp = models.IntegerField(max_length=9)
    bank = models.CharField(max_length=255)
    p_s = models.IntegerField(max_length=20)
    k_s = models.IntegerField(max_length=20)
    bik = models.IntegerField(max_length=9)

    def __str__(self):
        return self.name_legal_entity