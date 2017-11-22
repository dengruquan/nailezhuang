
# -*- coding: utf8 -*- 
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib import auth
from . import MilkCommon

@login_required
def index(request):
	href_dict = {}
	url_str = "http://127.0.0.1:8009/milk/%s/"
	for value in globals().items():
		if type(value[1])!=type(MilkCommon._f):
			continue
		fobj = globals()[value[0]]
		doc = fobj.__doc__
		if doc is None or doc.find("【") == -1:
			continue
		
		doc = doc.replace("【", "").replace("】","")
		href_dict[url_str % value[0]] = doc
	return render(request, 'milk/index.html', {"urldict":href_dict})
	
	
@login_required
def StasticsReq(request):
	'''【销售统计】'''
	now = MilkCommon.GetStrfTime(MilkCommon.GetNowTime())
	one_day_after = MilkCommon.GetStrfTime(MilkCommon.GetSomeDayAgo(-1))
	
	foodtype = MilkCommon.GetFoodDict()
	foodid_list = sorted(foodtype.keys())
	return render(request, 'milk/stasticsquery.html', {"now": now, "one_day_after": one_day_after, "foodtype": foodtype, "foodid_list" : foodid_list})
	
	
@login_required
def StasticsRes(request):
	'''销售统计结果查询'''
	POST = request.POST
	foodid = int(POST["foodid"])
	start_time = MilkCommon.AsDateTime(POST, name = "start_time")
	end_time = MilkCommon.AsDateTime(POST, name = "end_time")
	
	where_dict = {}
	if foodid:
		where_dict["foodid"] = foodid
	where_dict["start_time"] = start_time
	where_dict["end_time"] = end_time
	
	data_list = MilkCommon.GetStasticsResult(where_dict)
	html = MilkCommon.MakeDataHtml(data_list)
	return HttpResponse("".join(html))
	
	
	
@login_required
def VIPStasticsReq(request):
	'''月卡统计'''
	before = MilkCommon.GetStrfTime(MilkCommon.GetSomeDayAgo(-365))
	now = MilkCommon.GetStrfTime(MilkCommon.GetNowTime())
	
	viptype = MilkCommon.GetVIPInfoDict()
	vipid_list = sorted(viptype.keys())
	
	return render(request, 'milk/vipstasticsquery.html', {"now": now, "before": before, "viptype": viptype, "statype_dict" : MilkCommon.statype_dict})
	
	

def VIPStasticsRes(request):
	'''月卡统计结果查询'''
	POST = request.POST
	print("POST",POST)
	vipindex = POST["vipindex"]
	special = "所有"
	if vipindex.find("special"):
		vipindex = ""
	typeid = int(POST["typeid"])
	start_time = MilkCommon.AsDateTime(POST, name = "start_time")
	end_time = MilkCommon.AsDateTime(POST, name = "end_time")
	
	where_dict = {}
	if vipindex:
		where_dict["vipindex"] = vipindex
	where_dict["statypeid"] = typeid
	where_dict["start_time"] = start_time
	where_dict["end_time"] = end_time
	
	data_list = MilkCommon.GetVIPStasticsResult(where_dict, typeid)
	html = MilkCommon.MakeVIPDataHtml(data_list)
	return HttpResponse("".join(html))
	# return HttpResponse("POST %s" %vipindex)
	
	
	
	
