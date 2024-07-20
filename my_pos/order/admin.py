from django.contrib import admin
from .models import Person,Customers,Sales_Team,Product,OrderProduct,Orders,Category
# Register your models here.

admin.site.register(Person)
admin.site.register(Customers)
admin.site.register(Sales_Team)
admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(Orders)
admin.site.register(Category)