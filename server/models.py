import datetime

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    gLTF = models.FileField(upload_to='files/')
    date = models.DateTimeField(auto_now_add=True)
    height = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    mini_title = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-date']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Image_product(models.Model):
    image = models.ImageField(upload_to='image/products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фото Продукта'
        verbose_name_plural = 'Фото Продуктов'


class Work(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    adress = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class Image_work(models.Model):
    image = models.ImageField(upload_to='image/works/')
    work = models.ForeignKey(Work, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фото работы'
        verbose_name_plural = 'Фото работы'


class FAQ(models.Model):
    title = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image/news/')
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']


class Image_news(models.Model):
    image = models.ImageField(upload_to='image/news/')
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фото новости'
        verbose_name_plural = 'Фото новости'


class Feedback(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщение'
        ordering = ['-date']


class OrderItemUr(models.Model):
    order = models.ForeignKey('OrderUr', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class OrderItemFiz(models.Model):
    order = models.ForeignKey('OrderUr', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class OrderUr(models.Model):
    name = models.CharField(max_length=155)
    # series = models.CharField(
    #     max_length=7,
    #     verbose_name='серия пасспорта',
    #     blank=True
    # )
    inn = models.CharField(max_length=14, verbose_name='ИНН паспорта', blank=True, default=0000000000000)
    okpo = models.CharField(max_length=100, verbose_name='ОКПО', blank=True)
    bik = models.CharField(max_length=100, verbose_name='БИК', blank=True)
    r_c = models.CharField(max_length=100, verbose_name='р/с', blank=True)
    bank = models.CharField(max_length=155, verbose_name='Банк', blank=True)
    director = models.CharField(max_length=255, verbose_name='Директор')
    # date_of_issue = models.DateField(
    #     verbose_name='дата выдачи паспорта',
    #     blank=True
    # )
    # series_type = models.CharField(
    #     max_length=2,
    #     verbose_name="тип серии",
    #     choices=(("ID", 'ID'), ('AN', 'AN')),
    #     default='ID'
    # )
    adress = models.CharField(max_length=255, verbose_name='Адрес', blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100, default='+996')
    grunt = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True, default='Пусто')
    date = models.DateTimeField(auto_now_add=True)
    delivery = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    document = models.FileField('upload/files/dogovory/', blank=True, null=True)

    def __str__(self):
        return f'Заказ - {self.name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Юридические Заказы'
        ordering = ['-date']


class OrderFiz(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.EmailField()
    series = models.CharField(
        max_length=7,
        verbose_name='серия пасспорта',
        blank=True
    )
    date_of_issue = models.DateField(
        verbose_name='дата выдачи паспорта',
        blank=True
    )
    series_type = models.CharField(
        max_length=2,
        verbose_name="тип серии",
        choices=(("ID", 'ID'), ('AN', 'AN')),
        default='ID'
    )
    adress = models.CharField(max_length=255, verbose_name='Адрес', blank=True)
    phone = models.CharField(max_length=100)
    grunt = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True, default='Пусто')
    date = models.DateTimeField(auto_now_add=True)
    delivery = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField('upload/files/dogovory/', blank=True, null=True, default='/dogovor_ur.doc')

    def __str__(self):
        return f'Заказ - {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Физические Заказы'
        ordering = ['-date']
