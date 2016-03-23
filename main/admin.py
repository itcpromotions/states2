from django.contrib import admin
from main.models import State, StateCapital, City

# Register your models here.



class StateAdmin(admin.ModelAdmin):
	list_display = ('name', 'abbreviation')
	search_fields = ['name']


class StateCapitalAdmin(admin.ModelAdmin):
	list_display = ('name', 'state')

class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'state')
	search_fields = ['name']


admin.site.register(State, StateAdmin)
admin.site.register(StateCapital, StateCapitalAdmin)
admin.site.register(City, CityAdmin)