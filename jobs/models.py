from django.db import models
from django.urls import reverse


class Persons(models.Model):
    class Gender(models.IntegerChoices):
        MAN = 0, 'Муж'
        WOMAN = 1, 'Жен'

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
    gender = models.BooleanField(choices=Gender.choices, null=True, verbose_name="Пол")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Люди"
        verbose_name_plural = "Люди"

    def get_absolute_url(self):
        return reverse('person_detail', args=[str(self.pk)])

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

    def get_absolute_url(self):
        return reverse('partner_detail', args=[str(self.pk)])

class Order(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        WORK = 1, 'В работе'
        CLOSED = 2, 'Закрыто'

    order_name = models.IntegerField(verbose_name="Номер заявки")
    department = models.CharField(max_length=255, verbose_name="Департамент")
    location = models.CharField(max_length=255, verbose_name="Локация")
    vacancy = models.CharField(max_length=255, verbose_name="Вакансия")
    start_date = models.DateField(verbose_name="Дата начала")
    finish_date = models.DateField(verbose_name="Дата конец")
    start_time = models.TimeField(verbose_name="Начало смены")
    finish_time = models.TimeField(verbose_name="Конец смены")
    count_of_persons = models.IntegerField(verbose_name="Количество человек")
    dogovor = models.ForeignKey('Dogovor', on_delete=models.PROTECT, null=True, verbose_name="Договор")
    price_per_hour = models.IntegerField(verbose_name="Цена по договору")
    price_for_user = models.IntegerField(verbose_name="Цена для персонала")
    responsible_full_name = models.CharField(max_length=255, verbose_name="Ответственный")
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT, verbose_name="Статус")

    class Meta:
        verbose_name = "Заявки"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return str(self.order_name)

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.pk)])


class Dogovor(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        WORK = 1, 'В работе'
        CLOSED = 2, 'Закрыто'

    num_end_date = models.CharField(max_length=100, verbose_name="Дата заключения договора")
    sum_dogovor = models.IntegerField(verbose_name="Сумма договора")
    services = models.TextField(verbose_name="Услуги")
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT, verbose_name="Статус")
    legal_entity = models.ForeignKey('Partner', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Договора"
        verbose_name_plural = "Договора"

    def __str__(self):
        return str(self.num_end_date)
