#-*- coding:utf8 -*-

from django.db import models

# Create your models here.
class FoodType(models.Model):
	'''奶乐状物品类型'''
	foodname = models.CharField("物品名称", max_length=100, unique = True)
	foodprice = models.DecimalField("物品售价", max_digits=10, decimal_places=3, default=0)
	
	def __str__(self):
		return self.foodname
		

class FoodRecord(models.Model):
	'''奶乐状物品记录'''
	foodtype = models.ForeignKey(FoodType, on_delete=models.CASCADE)
	foodcnt = models.PositiveIntegerField("数量", default=1)
	foodmoney = models.DecimalField("金额", max_digits=30, decimal_places=3)
	foodtime = models.DateTimeField("时间")
	
	def __str__(self):
		return str(self.id)
	

class VIPType(models.Model):
	'''奶乐状月卡类型'''
	viptype = models.CharField("月卡类型名称", max_length=30, unique = True)
	
	def __str__(self):
		return self.viptype	
		

class VIPInfo(models.Model):
	'''奶乐状月卡用户信息'''
	vipindex = models.CharField("用户编号", max_length=20, unique = True)
	vipname = models.CharField("用户名", max_length=30)
	vipnumber = models.CharField("用户电话", max_length=15)
	viptype = models.ForeignKey(VIPType, on_delete=models.CASCADE)
	vipcnt = models.PositiveIntegerField("月卡牛奶数量", default=32)
	
	def __str__(self):
		return self.vipindex	
		
	
class VIPRecord(models.Model):
	'''奶乐状月卡使用记录'''
	viprecordname = models.ForeignKey(VIPInfo, on_delete=models.CASCADE)
	viprecordcnt = models.PositiveIntegerField("数量", default=1)
	viprecordtime = models.DateTimeField("时间")
	
	def __str__(self):
		return str(self.id)
		
	
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

	
	
	
	