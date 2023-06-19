import numpy as np
import pandas as pd
from django.db import models

# Create your models here.
from django.db import models
from simplepro.editor import fields

class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=64)

class Detect(models.Model):
    ip = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)


class LocalInfo(models.Model):
    #地理信息表
    ip=models.CharField(max_length=32,verbose_name='机构IP')
    address=models.CharField(max_length=128,verbose_name='地址')
    name=models.CharField(max_length=64,verbose_name='名称')
    mail=models.CharField(max_length=32,verbose_name='邮编')
    longitude=models.DecimalField(verbose_name='经度',max_digits=9, decimal_places=6)
    latitude = models.DecimalField(verbose_name='纬度',max_digits=9, decimal_places=6)



class TracertResult(models.Model):
    #source ,dist ,delays
    ip=models.CharField(max_length=32,verbose_name='本机IP')
    dist=models.CharField(max_length=32,verbose_name='目标IP')
    delays=models.CharField(max_length=1024,verbose_name='延迟列表')



class MyContent(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='标题')
    key_words = models.CharField(max_length=255, blank=True, null=True, verbose_name='关键字')
    sort = models.CharField(max_length=50, default='中药', blank=True, null=True, verbose_name='类别')
    summary = models.CharField(max_length=500, blank=True, null=True, verbose_name='摘要')
    cover = models.CharField(max_length=2048, blank=True, null=True, verbose_name='图1')
    cover2 = models.CharField(max_length=2048, blank=True, null=True, verbose_name='图2')
    cover3 = models.CharField(max_length=2048, blank=True, null=True, verbose_name='图3')
    cover4 = models.CharField(max_length=2048, blank=True, null=True, verbose_name='图4')
    cover5 = models.CharField(max_length=2048, blank=True, null=True, verbose_name='图5')
    cover6 = models.CharField(max_length=2048, blank=True, null=True, verbose_name='图6')
    cover7 = models.CharField(max_length=2048, blank=True, null=True, verbose_name='图7')
    html = fields.UETextField(max_length=65535, null=True, verbose_name='实体内容', help_text='实体内容（富文本）')
    release_time = models.DateTimeField(blank=True, null=True, verbose_name='发布时间', auto_now_add=True)
    update_time = models.DateField(blank=True, null=True, verbose_name='更新日期', auto_now=True)
    status = models.IntegerField(default=1, choices=((0, '隐藏'), (1, '正常')), verbose_name='实体状态')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '本草实体'
        verbose_name_plural = verbose_name



df=pd.read_csv('myapp/mdata/newlink1.csv')
for index,row in df.iterrows():
    cnt=7
    #print(type(row['img7']))
    if pd.isnull(row['img7']):
       print('yes')
       cnt=6
    if pd.isnull(row['img6']):
       cnt=5
    if pd.isnull(row['img5']):
       cnt=4
    if pd.isnull(row['img4']):
       cnt=3
    if pd.isnull(row['img3']):
        cnt = 2
    if pd.isnull(row['img2']):
       cnt=1
    if pd.isnull(row['img1']):
       cnt=0

    print(cnt)



    if cnt==7:
        if pd.isnull(row['summary']):#释名summary为空
            MyContent.objects.create(title=row['name'],key_words=row['name'],sort=row['sort'],cover=row['img1'],
                                     cover2=row['img2'],
                                     cover3=row['img3'],
                                     cover4=row['img4'],
                                     cover5=row['img5'],
                                     cover6=row['img6'],
                                     cover7=row['img7'],
                                     )
        else:
            MyContent.objects.create(title=row['name'], key_words=row['name'], sort=row['sort'], cover=row['img1'],
                                     cover2=row['img2'],
                                     cover3=row['img3'],
                                     cover4=row['img4'],
                                     cover5=row['img5'],
                                     cover6=row['img6'],
                                     cover7=row['img7'],
                                     summary=row['summary']
                                     )
    if cnt==6:
        if pd.isnull(row['summary']):  # 释名summary为空
            MyContent.objects.create(title=row['name'],key_words=row['name'],sort=row['sort'],cover=row['img1'],
                                     cover2=row['img2'],
                                     cover3=row['img3'],
                                     cover4=row['img4'],
                                     cover5=row['img5'],
                                     cover6=row['img6']
                                     )
        else:
            MyContent.objects.create(title=row['name'], key_words=row['name'], sort=row['sort'], cover=row['img1'],
                                     cover2=row['img2'],
                                     cover3=row['img3'],
                                     cover4=row['img4'],
                                     cover5=row['img5'],
                                     cover6=row['img6'],
                                     summary=row['summary']
                                     )

    if cnt==5:
        if pd.isnull(row['summary']):  # 释名summary为空
            MyContent.objects.create(title=row['name'],key_words=row['name'],sort=row['sort'],cover=row['img1'],
                                     cover2=row['img2'],
                                     cover3=row['img3'],
                                     cover4=row['img4'],
                                     cover5=row['img5']

                                     )
        else:
            MyContent.objects.create(title=row['name'], key_words=row['name'], sort=row['sort'], cover=row['img1'],
                                     cover2=row['img2'],
                                     cover3=row['img3'],
                                     cover4=row['img4'],
                                     cover5=row['img5'],
                                     summary=row['summary']
                                     )

    if cnt==4:
        if pd.isnull(row['summary']):  # 释名summary为空
            MyContent.objects.create(title=row['name'],key_words=row['name'],sort=row['sort'],cover=row['img1'],
                                     cover2=row['img2'],
                                     cover3=row['img3'],
                                     cover4=row['img4']
                                 )
        else:
            MyContent.objects.create(title=row['name'], key_words=row['name'], sort=row['sort'], cover=row['img1'],
                                     cover2=row['img2'],
                                     cover3=row['img3'],
                                     cover4=row['img4'],
                                     summary=row['summary']
                                     )
    if cnt==3:
        if pd.isnull(row['summary']):  # 释名summary为空
            MyContent.objects.create(title=row['name'],key_words=row['name'],sort=row['sort'],cover=row['img1'],
                                     cover2=row['img2'],
                                     cover3=row['img3']
                                     )
        else:
            MyContent.objects.create(title=row['name'], key_words=row['name'], sort=row['sort'], cover=row['img1'],
                                     cover2=row['img2'],
                                     cover3=row['img3'],

                                     summary=row['summary']
                                     )
    if cnt==2:
        if pd.isnull(row['summary']):  # 释名summary为空
            MyContent.objects.create(title=row['name'],key_words=row['name'],sort=row['sort'],cover=row['img1'],
                                     cover2=row['img2']

                                     )
        else:
            MyContent.objects.create(title=row['name'], key_words=row['name'], sort=row['sort'], cover=row['img1'],
                                     cover2=row['img2'],

                                     summary=row['summary']
                                     )
    if cnt==1:
        if pd.isnull(row['summary']):  # 释名summary为空
            MyContent.objects.create(title=row['name'],key_words=row['name'],sort=row['sort'],cover=row['img1'],

                                     )
        else:
            MyContent.objects.create(title=row['name'], key_words=row['name'], sort=row['sort'], cover=row['img1'],

                                     summary=row['summary']
                                     )
    if cnt==0:
        if pd.isnull(row['summary']):  # 释名summary为空
            MyContent.objects.create(title=row['name'],key_words=row['name'],sort=row['sort']
                                     )
        else:
            MyContent.objects.create(title=row['name'], key_words=row['name'], sort=row['sort'],

                                     summary=row['summary']
                                     )

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self): return f'{self.product} - {self.author.username}'