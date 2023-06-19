from django.test import TestCase

# Create your tests here.
# 导入 unittest 模块
import unittest
# 导入 Django 的 TestCase 类
from django.test import TestCase
# 导入模型类
from myapp.models import LocalInfo, TracertResult


# 编写一个测试类，继承自 Django 的 TestCase 类
class MyModelTestCase(TestCase):
    # 设置测试固件，即测试数据
    fixtures = ['mytestdata.json']
    # 编写测试方法，测试模型类的保存方法
    def test_save_method(self):
        # 创建一个模型实例
        mymodel = LocalInfo.objects.create(ip='211.71.149.53',
                                           address='BJFU',
                                           name='EDUCATION',
                                           mail='xxx@qq.com',
                                           longitude=116.5,
                                           latitude=40.8)
        # 断言模型实例的属性值保存的一致
        self.assertEqual(mymodel.ip, '211.71.149.53')
        self.assertEqual(mymodel.address, 'BJFU')
        self.assertEqual(mymodel.name, 'EDUCATION')
        self.assertEqual(mymodel.mail, 'xxx@qq.com')
        self.assertEqual(mymodel.longitude, 116.5)
        self.assertEqual(mymodel.latitude, 40.8)
    # 编写测试方法，测试模型类的查询方法
    def test_query_method(self):
        # 查询数据库中的所有模型实例
        mymodels = LocalInfo.objects.all()
        # 断言查询结果的长度与期望的一致
        self.assertEqual(len(mymodels), 32)
        #断言模型实例的属性值与期望的一致
        self.assertEqual(mymodels[0].ip, '211.71.149.53')
        self.assertEqual(mymodels[0].address, 'BJFU')
        self.assertEqual(mymodels[0].name, 'EDUCATION')
        self.assertEqual(mymodels[0].mail, 'xxx@qq.com')
        self.assertEqual(mymodels[0].longitude, 116.5)
        self.assertEqual(mymodels[0].latitude, 40.8)



# 编写测试方法，测试模型类的保存方法
    def test_save_method1(self):
        # 创建一个模型实例
        mymodel = TracertResult.objects.create(ip='211.71.149.53',
                                          dist='172.27.237.110',
                                          delays=''
                                          )
        # 断言模型实例的属性值保存的一致
        self.assertEqual(mymodel.ip, '211.71.149.53')
        self.assertEqual(mymodel.dist, '172.27.237.110')
        self.assertEqual(mymodel.delays, '')

    # 编写测试方法，测试模型类的查询方法
    def test_query_method1(self):
        # 查询数据库中的所有模型实例
        mymodels = TracertResult.objects.all()
        # 断言查询结果的长度与期望的一致
        self.assertEqual(len(mymodels), 188)
        #断言模型实例的属性值与期望的一致
        self.assertEqual(mymodels[0].ip, '211.71.149.53')
        self.assertEqual(mymodels[0].dist, '172.27.237.110')
        self.assertEqual(mymodels[0].delays, '')

