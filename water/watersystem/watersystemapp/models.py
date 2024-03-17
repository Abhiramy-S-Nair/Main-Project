from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime



class CustomUser(AbstractUser):
    firstname = models.TextField(max_length=100, default="")
    lastname = models.TextField(max_length=100, default="")
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=128, default="")
   
   

    def __str__(self):
        return self.password
    

class LoginDetail(models.Model):
    login_id = models.AutoField(primary_key=True)  # Autogenerated primary key
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Foreign key to the Customer model
    login_time = models.DateTimeField(auto_now_add=True)  # Time of login

    def __str__(self):
        return self.username.username 
    
    
class District(models.Model):
    # Primary key field with the format disXXX (e.g., dis001, dis002, etc.)
    district_id = models.AutoField(primary_key=True, editable=False)

    # District name field
    district_name = models.CharField(max_length=100)

    

    def __str__(self):
        return self.district_name
    
    
class WaterProduct(models.Model):
    product_id = models.AutoField(primary_key=True, editable=False)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    

    def __str__(self):
        return self.product_name
    
class City(models.Model):
    City_ID = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name
    

class Order(models.Model):
    order_id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(WaterProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    delivery_date_time = models.DateTimeField(default=datetime.now)
    order_time = models.DateTimeField(auto_now_add=True)
     

    def __str__(self):
        return f"Order {self.order_id}"
    
class Address(models.Model):
    address_id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    pincode = models.CharField(max_length=10)
    City_ID = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    street = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"Address {self.address_id}"
    
class OrderAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.order_id} - Address {self.address_id}"




class UserAddress(models.Model):
    address_id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    pincode = models.CharField(max_length=10)
    
    City_ID = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"Address {self.address_id}"
    
class UserOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # Represented in gallons
    delivery_date_time = models.DateTimeField()
    payment_method = models.CharField(max_length=20)
    special_instructions = models.TextField(blank=True)  # Optional field for instructions

    def __str__(self):
        return f"Order ID: {self.order_id}, User: {self.address.user.username}"
    

class WorkerProfile(models.Model):
    worker_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(blank=True)
    services = models.CharField(max_length=255, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    availability = models.CharField(max_length=100, blank=True)
    terms = models.BooleanField(default=False)

    def __str__(self):
        return str(self.worker_id)
    

class AddService(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    

class ServiceRequest(models.Model):
    Request_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use the User model as a foreign key
    service_name = models.ForeignKey(AddService, on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    water_level = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    street = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)  # Assuming you have a City model
    district = models.ForeignKey(District, on_delete=models.CASCADE)  # Assuming you have a District model
    zip_code = models.CharField(max_length=10)
    request_date_time = models.DateTimeField()
    

    def __str__(self):
        return str(self.Request_id)
    

class UploadedFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='uploads/pdf/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    



class DrinkingWaterProduct(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def reduce_stock(self, quantity_to_reduce):
        if self.quantity >= quantity_to_reduce:
            self.quantity -= quantity_to_reduce
            return True
        return False
    
class WaterOrder(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(DrinkingWaterProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    delivery_date_time = models.DateTimeField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    request_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order for {self.quantity} {self.product.name}'
    


class AssignedWorker(models.Model):
    WORK_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    assigned_worker_id = models.AutoField(primary_key=True)  # Specify your primary key field
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE)
    work_status = models.CharField(max_length=20, choices=WORK_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"AssignedWorker {self.assigned_worker_id} - ServiceRequest {self.service_request.Request_id} - Worker {self.worker.worker_id} - Status {self.work_status}"





class LeaveApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    leave_application_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    medical_certificate = models.FileField(upload_to='medical_certificates/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Leave Application #{self.leave_application_id} - {self.user.username}"
    

class Orders(models.Model):
    SERVICE_CHOICES = [
        ('water_delivery', 'Water Delivery'),
        ('borewell_cleaning', 'Borewell Cleaning'),
        ('water_tank_cleaning', 'Water Tank Cleaning'),
        ('well_cleaning', 'Well Cleaning'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    phone = models.CharField(max_length=15)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=10)

    quantity = models.PositiveIntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    waterlevel = models.FloatField(blank=True, null=True)

    request_date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order {self.id} for {self.user.username} - {self.get_service_display()} - {self.get_status_display()}"



class OrderAssignment(models.Model):
    STATUS_CHOICES = [
        ('assigned', 'Assigned'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE)
   
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='assigned')

    def __str__(self):
        return f"Assignment for Order {self.order.id} to Worker {self.worker.worker_id} "
    

class OrderWorkerAssignment(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"OrderWorkerAssignment - Order {self.order.id} assigned to Worker {self.worker.worker_id}"
    

class Payment(models.Model):
    order_assignment = models.ForeignKey(OrderWorkerAssignment, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default='Pending')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order_assignment.order.id} by User {self.user.username}"
    


    from django.db import models
from django.contrib.auth.models import User

class DeliveryBoy(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    profile_photo = models.ImageField(upload_to='profile_photos/')
    driving_license = models.FileField(upload_to='driving_licenses/')
    identity_proof = models.FileField(upload_to='identity_proofs/')

    def __str__(self):
        return self.user.username

    
# delivery_app/models.py
from django.db import models

class Vendor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    gst_number = models.CharField(max_length=15)
    profile_photo = models.ImageField(upload_to='vendor_profile_photos/')
    identity_proof = models.FileField(upload_to='vendor_identity_proofs/')

# delivery_app/models.py
from django.db import models
from django.contrib.auth.models import User

class VendorDetails(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    gst_number = models.CharField(max_length=15)
    profile_photo = models.ImageField(upload_to='vendor_profile_photos/')
    identity_proof = models.FileField(upload_to='vendor_identity_proofs/')
    

def __str__(self):
    return f"VendorDetails for {self.user.username}"




    
# models.py

from django.db import models
from django.contrib.auth.models import User

class StockTransaction(models.Model):
    product = models.ForeignKey('VendorProduct', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50)  # 'in_stock', 'sold', 'restocked'
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class ProductPriceHistory(models.Model):
    product = models.ForeignKey('VendorProduct', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateField(auto_now_add=True)

# models.py
from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class VendorProduct(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField(default=0)  # New field for stock quantity

    def save(self, *args, **kwargs):
        if self.pk is not None:
            StockTransaction.objects.create(
                product=self,
                transaction_type='restocked',
                quantity=self.stock_quantity
            )
        super().save(*args, **kwargs)

    def restock_product(self, quantity):
        self.stock_quantity += quantity
        self.save()
        StockTransaction.objects.create(
            product=self,
            transaction_type='restocked',
            quantity=quantity
        )

    def sell_product(self, quantity):
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            self.save()
            StockTransaction.objects.create(
                product=self,
                transaction_type='sold',
                quantity=quantity
            )
            return True
        return False

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if self.pk is not None:
            ProductPriceHistory.objects.create(
                product=self,
                price=self.price,
                offer=self.offer
            )
        super().save(*args, **kwargs)

    def get_price_history(self):
        return ProductPriceHistory.objects.filter(product=self).order_by('timestamp')

    def __str__(self):
        return self.name

#from django.db import models
#from django.contrib.auth import get_user_model
#from django.utils import timezone
#from django.db.models.signals import post_save
#from django.dispatch import receiver

#User = get_user_model()

#   user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#    product = models.ForeignKey(VendorProduct, on_delete=models.CASCADE)
 #   quantity = models.PositiveIntegerField()
  #  timestamp = models.DateTimeField(default=timezone.now)

   # def __str__(self):
     #   return f"{self.user.username}'s Cart - {self.product.name}"
    
class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(VendorProduct, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"
class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(VendorProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class DeliveryAddress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
      
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
    locality = models.CharField(max_length=255)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    alternate_phone_number = models.CharField(max_length=10, blank=True, null=True)
    address_type_choices = [
        ('home', 'Home'),
        ('work', 'Work'),
    ]
    address_type = models.CharField(max_length=10, choices=address_type_choices)
    
    # Status choices: 'in_progress', 'out_for_delivery', 'completed'
    
    def __str__(self):
        return f"{self.user.username}'s Delivery Address"
class ProductOrder(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(VendorProduct, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey('ProductOrder', on_delete=models.CASCADE)
    product = models.ForeignKey(VendorProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
    
from django.db import models
from django.contrib.auth.models import User

class DeliveryBoys(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos')
    identity_proof = models.ImageField(upload_to='identity_proofs')
    driving_license = models.ImageField(upload_to='driving_licenses')

    def __str__(self):
        return f"{self.user.username}'s Delivery Boy Details"

from django.db import models
from django.contrib.auth.models import User

class DeliveryBoyAddress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
    locality = models.CharField(max_length=255)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    alternate_phone_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Delivery Boy Address"
