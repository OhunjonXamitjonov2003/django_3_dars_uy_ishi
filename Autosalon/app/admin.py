from django.contrib import admin
from .models import Brand,Car,Color
# Register your models here.




class CarAdmin(admin.ModelAdmin):
    list_display = ('id','brand','car_name','role','price','color','created','update','published')
    list_display_links = ('car_name',)
    list_editable = ('published','brand','role','price','color')
    search_fields = ('car_name','brand')
admin.site.register(Car,CarAdmin)
admin.site.register(Brand)
admin.site.register(Color)


