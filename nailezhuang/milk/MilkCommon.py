#-*- coding:utf8 -*-
import datetime
import sqlite3
from .models import FoodType, VIPInfo

time_format = "%Y-%m-%d %H:%M:%S"
statype_dict = {0:"每次喝奶数量", 1: "总共喝奶数量"}
dbname = "db.sqlite3"
sel_sql = "select foodname, sum(foodcnt), sum(foodmoney) from milk_foodrecord as fr join milk_foodtype as ft where fr.foodtype_id = ft.id and %s group by foodtype_id;"
vip_selper_sql = "select vipindex, vipname, viprecordcnt, viprecordtime from milk_viprecord as viprecord join milk_vipinfo as vipinfo where viprecord.viprecordname_id = vipinfo.vpiindex and %s ;"
vip_selsum_sql = "select vipindex, vipname, sum(viprecordcnt) from milk_viprecord as viprecord join milk_vipinfo as vipinfo where viprecord.viprecordname_id = vipinfo.vpiindex and %s group by viprecordname;;"

# vip_selper_sql = "select viprecordcnt from  milk_viprecord as vipinfo where %s ;"
# vip_selsum_sql = "select viprecordcnt from  milk_viprecord as vipinfo where %s ;"

def GetNowTime():
	'''返回当前时间'''
	tmp = datetime.datetime.now().strftime("%Y,%m,%d")
	print("tmp", tmp)
	return datetime.datetime(*eval(tmp))
	
def GetSomeDayAgo(day = 1):
	'''返回指定天数前的时间，由day进行控制'''
	return GetNowTime()- datetime.timedelta(days = day)
	
	
def GetStrfTime(timeobj):
	'''返回指定的时间格式'''
	return timeobj.strftime("{}".format(time_format))
	
	
def AsDateTime(GET_POST, name = "datetime"):
	return datetime.datetime.strptime(GET_POST[name], "{}".format(time_format))
	
	
def GetFoodDict():
	'''获取所有物品字典'''
	foodtype = FoodType.objects.all()
	food_dict = {0: "所有"} #{id:foodname}
	for foodobj in foodtype:
		food_dict[foodobj.id] = foodobj.foodname
		
	return food_dict
	

def ConnectDB(dbname):
	'''
	连接到数据库
	@parameter dbname: 数据库名
	'''
	return sqlite3.connect(dbname)
	

def MakeWhereSql(where_dict):
	'''制作sql中where条件'''
	where_list = []
	if "foodid" in where_dict:
		where_list.append("fr.foodtype_id = %d" % where_dict["foodid"])
	where_list.append("foodtime >= '{}'".format(where_dict["start_time"]))
	where_list.append("foodtime <= '{}'".format(where_dict["end_time"]))
	
	return " and ".join(where_list)
	
	
def MakeVIPWhereSql(where_dict):
	'''制作sql中where条件'''
	where_list = []
	if "vipindex" in where_dict:
		where_list.append("vipinfo.vipindex = %s" % where_dict["vipindex"])
	where_list.append("viprecordtime >= '{}'".format(where_dict["start_time"]))
	where_list.append("viprecordtime <= '{}'".format(where_dict["end_time"]))
	
	return " and ".join(where_list)
	
	
def GetStasticsResult(where_dict):
	'''
	获取指定条件下的销售记录
	@parameter: where_dict: {"foodid": id, "start_time": time, "end_time": time}
	@return : [[foodname, cnt, money]]
	'''
	con = ConnectDB(dbname)
	# print(sel_sql % MakeWhereSql(where_dict))
	with con as cur:
		cur = cur.execute(sel_sql % MakeWhereSql(where_dict))
		ret = cur.fetchall()
		cur.close()
			
	return ret
		

def MakeDataHtml(data_list):
	'''
	制作html页面内容
	'''
	html = [
	'<!DOCTYPE html><html><head><title>销售统计</title><meta charset="UTF-8"></head><body><form>']
	
	foodname = "物品名称"
	foodcnt = "数量"
	foodmoney = "金额"
	sumname = "总销售额："
	sum_money = 0
	# html.append('<table border="1px" cellpadding = "20" cellspacing="50" style= "border-collapse:collapse"><thead><tr><th>{}</th><th>{}</th><th>{}</th>'.format(foodname, foodcnt, foodmoney))
	if data_list :
		for name, cnt, money in data_list:
			sum_money += money
		
		html.append("<font size='6'>%s%s</font>" % (sumname, sum_money))
		html.append("<br/>")
		
		html.append('<table border="1px" cellpadding = "20" cellspacing="50" style= "border-collapse:collapse"><thead><tr><th>{}</th><th>{}</th><th>{}</th>'.format(foodname, foodcnt, foodmoney))
	
		for name, cnt, money in data_list:
			html.append("<tr><td> %s </td><td> %s </td><td> %s </td></tr>" % (name, cnt, money))
			print("sum_money", sum_money)
			
	html.append("</thead></table>")
	html.append("</form></body></html>")
	
	return html
	
def MakeIndexHtml(index_list):
	html = []
	# for urlname, funname in index_list:
		# html.append('<a href="{% url {} %}">{}</a>')
	
	# html.append("</html>")
	return html
	
	
	
def _f():pass


def GetVIPInfoDict():
	'''获取月卡用户信息字典'''
	vipinfo = VIPInfo.objects.all()
	vip_dict = {0: "所有"} #{id:foodname}
	for vipobj in vipinfo:
		vip_dict[vipobj.id] = vipobj.vipindex
		
	return vip_dict
	
	
def GetVIPStasticsResult(where_dict, typeid):
	'''
	获取指定条件下的月卡用户喝奶统计
	@parameter: where_dict: {"vipid": vipid, "start_time": time, "end_time": time}
	@parameter: typeid: 数据统计类型{0:"每次喝奶数量", 1: "总共喝奶数量"}
	@return : [[foodname, cnt, money]]
	'''
	con = ConnectDB(dbname)
	# print(sel_sql % MakeVIPWhereSql(where_dict))
	sql = vip_selsum_sql if typeid else vip_selper_sql 
	with con as cur:
		cur = cur.execute(sql % MakeVIPWhereSql(where_dict))
		ret = cur.fetchall()
		cur.close()
			
	return ret
	

def MakeVIPDataHtml(data_list):
	'''
	制作html页面内容
	'''
	html = [
	'<!DOCTYPE html><html><head><title>销售统计</title><meta charset="UTF-8"></head><body><form>']
	
	foodname = "物品名称"
	foodcnt = "数量"
	foodmoney = "金额"
	sumname = "总销售额："
	sum_money = 0
	# html.append('<table border="1px" cellpadding = "20" cellspacing="50" style= "border-collapse:collapse"><thead><tr><th>{}</th><th>{}</th><th>{}</th>'.format(foodname, foodcnt, foodmoney))
	if data_list :
		for name, cnt, money in data_list:
			sum_money += money
		
		html.append("<font size='6'>%s%s</font>" % (sumname, sum_money))
		html.append("<br/>")
		
		html.append('<table border="1px" cellpadding = "20" cellspacing="50" style= "border-collapse:collapse"><thead><tr><th>{}</th><th>{}</th><th>{}</th>'.format(foodname, foodcnt, foodmoney))
	
		for name, cnt, money in data_list:
			html.append("<tr><td> %s </td><td> %s </td><td> %s </td></tr>" % (name, cnt, money))
			print("sum_money", sum_money)
			
	html.append("</thead></table>")
	html.append("</form></body></html>")
	
	return html	
	
if __name__ == "__main__":
	GET_POST = {"start_time": "2017-11-16 09:53:44"}
	# print(AsDateTime(GET_POST, name = "start_time"))
	where_dict =  { "start_time" : "2017-11-16 09:53:44", "end_time" : "2017-11-16 09:53:44"}
	# print MakeWhereSql(where_dict)
	# for value in globals().items():
		# if type(value[1])==type(_f):
			# print value[0] 
	pass