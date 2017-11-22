from django.contrib import admin

# Register your models here.

from .models import FoodType, FoodRecord, VIPType, VIPInfo, VIPRecord
class FoodTypeAdmin(admin.ModelAdmin):
	'''物品名称排序'''
	list_display = ('foodname', 'foodprice')
	search_fields=("foodname", )
	ordering = ("foodprice",)
	
class FoodRecordAdmin(admin.ModelAdmin):
	ordering = ("foodtime",)
	
	
class VIPTypeAdmin(admin.ModelAdmin):
	ordering = ("viptype",)
	

class VIPInfoAdmin(admin.ModelAdmin):
	search_fields = ("vipindex", 'vipname', "vipnumber")
	list_display = ('vipindex', 'vipname', "vipnumber", "viptype", "vipcnt")
	ordering = ("vipindex",)
	
	
admin.site.register(FoodType, FoodTypeAdmin)
admin.site.register(FoodRecord, FoodRecordAdmin)
admin.site.register(VIPType, VIPTypeAdmin)
admin.site.register(VIPInfo, VIPInfoAdmin)
admin.site.register(VIPRecord)