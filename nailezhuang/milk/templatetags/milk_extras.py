# from django import template
from django import template

register = template.Library()

# @register.filter(name='get_item')
def get_item(dict, key):
	return dict.get(key)
