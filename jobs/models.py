from django.db import models


class Persons(models.Model):
    class Gender(models.IntegerChoices):
        MEN = 0, 'Муж'
        Woman = 1, 'Жен'

    # class Status(models.IntegerChoices):
    #     DRAFT = 0, 'Черновик'
    #     PUBLISHED = 1, 'Опубликовано'

    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    date_of_birth = models.DateField(verbose_name="Дата рождления", blank=True)
    # photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
    #                           blank=True, null=True, verbose_name="Фото")
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    city = models.CharField(max_length=255, verbose_name="Город")
    size = models.CharField(max_length=255, verbose_name="Размер одежды", blank=True)
    last_job = models.CharField(max_length=255, verbose_name="Последнее место работы", blank=True)
    gender = models.CharField(max_length=255, verbose_name="Пол")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.full_name


    class Meta:
        verbose_name = "Люди"
        verbose_name_plural = "Люди"


class Partner(models.Model):
    name_legal_entity = models.CharField(max_length=255, verbose_name="Контрагент")
    ogrn = models.IntegerField(verbose_name="ОГРН")
    legal_address = models.CharField(max_length=255, verbose_name="Адрес")
    inn = models.IntegerField(verbose_name="ИНН")
    kpp = models.IntegerField(verbose_name="КПП")
    bank = models.CharField(max_length=255, verbose_name="Банк")
    p_s = models.IntegerField(verbose_name="р/с")
    k_s = models.IntegerField(verbose_name="к/с")
    bik = models.IntegerField(verbose_name="БИК")

    def __str__(self):
        return self.name_legal_entity

    class Meta:
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенты"