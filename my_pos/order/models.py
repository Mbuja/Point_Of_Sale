from django.db import models

# Create your models here.
class Person(models.Model):
    id_no= models.CharField(max_length=13,unique=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,unique=True)
    address = models.CharField(max_length=255)


    def __str__(self):
        temp_name =self.fname[0]
        temp_name = temp_name + "."+self.lname
        return temp_name


class Customers(models.Model):
    person =models.ForeignKey(Person,on_delete=models.CASCADE)
    
    def __str__(self):
        return F"{self.person.fname[0]}.{self.person.lname}"


class  Sales_Team(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)

    def __str__(self):
        return F"{self.person.fname[0]}.{self.person.lname}"


class Category(models.Model):
    COLD_BEVERAGES = 1
    HOT_BEVERAGES = 2
    BREAKFAST = 3
    LUNCH = 4
    SNACKS = 5

    TYPES = [
        (COLD_BEVERAGES, "Cold Beverages"),
        (HOT_BEVERAGES, "Hot Beverages"),
        (BREAKFAST, "Breakfast"),
        (LUNCH, "Lunch"),
        (SNACKS, "Snacks"),
    ]
    
    category_name = models.PositiveSmallIntegerField(choices=TYPES)

    def __str__(self):
        return dict(self.TYPES)[self.category_name]


class Product(models.Model):
    product_name =models.CharField(max_length=80)
    description = models.TextField(300)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}"


class Orders(models.Model):
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    sales_person = models.ForeignKey(Sales_Team,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,through="OrderProduct")
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
        return F"Order {self.id} on {self.order_date}"

#An intermediate table to allow for many products in single order
class OrderProduct(models.Model):
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.product_name} in Order {self.order.id}"


