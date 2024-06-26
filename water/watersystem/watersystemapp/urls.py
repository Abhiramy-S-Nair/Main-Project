from django.urls import path
from watersystemapp import views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('indexecommerce.html', views.indexecommerce, name='indexecommerce'),
    path('indexproduct.html', views.indexproduct, name='indexproduct'),
    path('product-section/', views.product_section_view, name='product_section'),

    path('termsforwater.html', views.termsforwater, name='termsforwater'),
    path('termsforcleaning.html', views.termsforcleaning, name='termsforcleaning'),
    path('views.html', views.views, name='views'),
    path('orders.html', views.orders, name='orders'),
    path('about.html', views.about, name='about'),
    path('products.html', views.products, name='products'),
    path('blog.html', views.blog, name='blog'),
    path('book.html', views.book, name='book'),
    path('adminorder.html', views.adminorder, name='adminorder'),
    path('logout/', views.logout, name='logout'),
    path('cleaning.html', views.cleaning, name='cleaning'),
    path('booking.html', views.booking, name='booking'),
    path('contact.html', views.contact, name='contact'),
    path('services.html', views.services, name='services'),
    path('login.html', views.user_login, name='user_login'),
    path('signup.html', views.signup, name='signup'),
    path('admindashboard.html', views.admindashboard, name='admindashboard'),
    path('workmanagerdashboard.html', views.workmanagerdashboard, name='workmanagerdashboard'),
    path('vendordashboard.html', views.vendordashboard, name='vendordashboard'),
     path('vendor_profile/', views.vendor_profile, name='vendor_profile'),
      path('vendor_profile/', views.vendor_profile, name='vendor_profile'),
    path('edit_vendorprofile/', views.edit_vendor_profile, name='edit_vendor_profile'),
    path('deliveryboydashboard.html', views.deliveryboydashboard, name='deliveryboydashboard'),
    path('workerdashboard.html', views.workerdashboard, name='workerdashboard'),
    path('user_list.html', views.user_list, name='user_list'),
    path('worker_list.html', views.worker_list, name='worker_list'),
    path('request_worker_signup.html', views.request_worker_signup, name='request_worker_signup'),
    path('admin_worker_requests.html', views.admin_worker_requests, name='admin_worker_requests'),
    path('delete_worker/<int:worker_id>/', views.delete_worker, name='delete_worker'),
    path('add_worker.html', views.add_worker, name='add_worker'),
    path('userprofile.html', views.userprofile, name='userprofile'),
    path('deliveryboyprofile.html', views.deliveryboyprofile, name='deliveryboyprofile'),

     path('file_details.html', views.file_details, name='file_details'),
    path('edit_file/<int:file_id>/', views.edit_file, name='edit_file'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('vendor_signup.html', views.vendor_signup, name='vendor_signup'),
    path('deliveryboy_signup.html', views.deliveryboy_signup, name='deliveryboy_signup'),
    path('add_workmanager.html', views.add_workmanager, name='add_workmanager'),
    path('admin.html', views.admin, name='admin'),
    path('all_worker_profiles/', views.all_worker_profiles, name='all_worker_profiles'),
    path('vendor_registration/', views.vendor_registration, name='vendor_registration'),
     path('vendor_details.html', views.vendor_details, name='vendor_details'),
     path('vendor_join/', views.vendor_join, name='vendor_join'),
    path('accept_vendor/<int:vendor_id>/', views.accept_vendor, name='accept_vendor'),
    path('delete_vendor/<int:vendor_id>/', views.delete_vendor, name='delete_vendor'),



    path('adddistrict.html', views.adddistrict, name='adddistrict'),
     path('viewrequest.html', views.viewrequest, name='viewrequest'),
    path('addproduct.html', views.addproduct, name='addproduct'),
    path('address.html', views.address, name='address'),
     path('productview.html', views.productview, name='productview'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
     path('edit_profile/', views.edit_profile, name='edit_profile'),
     path('drinking_water_products/', views.drinking_water_products, name='drinking_water_products'),
    
     path('book_product/', views.book_product, name='book_product'), 
     path('orderaddress/<int:order_id>/<int:address_id>/', views.orderaddress, name='orderaddress'),
    path('order_address_details/<int:order_id>/', views.order_address_details, name='order_address_details'),
    path('all_orders_details/', views.all_orders_details, name='all_orders_details'),
       path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
     path('adding.html', views.adding, name='adding'),
    path('add_city.html', views.add_city, name='add_city'),
    path('add_service.html', views.add_service, name='add_service'),
    path('update_worker_profile/', views.update_worker_profile, name='update_worker_profile'),
     path('service_details.html', views.service_details, name='service_details'),
     path('service_users.html', views.service_users, name='service_users'),
    path('confirm_order/<int:order_id>/', views.confirm_order, name='confirm_order'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('submit_cleaning_request/', views.submit_cleaning_request, name='submit_cleaning_request'),

     path('upload_file.html', views.upload_file, name='upload_file'),
    path('file_upload_success/', views.file_upload_success, name='file_upload_success'),

    path('view_uploaded_files/', views.view_uploaded_files, name='view_uploaded_files'),
     path('product_list.html', views.product_list, name='product_list'),
    path('create_order/<int:product_id>/', views.create_order, name='create_order'),
    path('view_water_orders/', views.view_water_orders, name='view_water_orders'),

     path('add_drinking_water.html', views.add_drinking_water, name='add_drinking_water'),
    path('add_drinking_water_success/', views.add_drinking_water_success, name='add_drinking_water_success'),
    
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    
    path('registered_users.html', views.registered_users, name='registered_users'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('assign_worker/<str:district>/', views.assign_worker, name='assign_worker'),
    path('assign_cleaningworker/<str:district>/', views.assign_worker, name='assign_cleaningworker'),
     path('assign_cleaningworker/<str:district>/', views.assign_cleaning_worker, name='assign_cleaning_worker'),
      path('apply_leave/', views.apply_leave, name='apply_leave'),
       path('view_leave_applications/', views.view_leave_applications, name='view_leave_applications'),
        path('approve_or_delete_leave/', views.approve_or_delete_leave, name='approve_or_delete_leave'),
         path('my_leave_details/', views.my_leave_details, name='my_leave_details'),
path('submit_order/', views.submit_order, name='submit_order'),
 path('orders_list/', views.orders_list, name='orders_list'),
  path('delivery_opportunities.html', views.delivery_opportunities, name='delivery_opportunities'),
    path('vendor_join.html', views.vendor_join, name='vendor_join'),
   
    path('delivery_details.html', views.delivery_details, name='delivery_details'),  # Add this line
    path('delivery_recruitment.html', views.delivery_recruitment, name='delivery_recruitment'),
    path('order/<int:order_id>/delete/', views.delete_order, name='delete_order'),
      path('confirm_order/<int:order_id>/', views.confirm_order, name='confirm_order'),
   
    path('assigning_worker/<int:order_id>/', views.assigning_worker, name='assigning_worker'),
    path('process_assignment/<int:order_id>/', views.process_assignment, name='process_assignment'),
    path('assignment_success/', views.assignment_success, name='assignment_success'),
     path('worker_assignment_details/', views.worker_assignment_details, name='worker_assignment_details'),
      path('complete_order/<int:order_id>/', views.complete_order, name='complete_order'),
      path('order_history/', views.order_history, name='order_history'),
       path('payment_page/<int:order_id>/<str:username>/', views.payment_page, name='payment_page'),
        path('process_payment/<int:order_id>/', views.process_payment, name='process_payment'),
        path('payment_history/', views.payment_history, name='payment_history'),
         path('razorpay-payment/', views.razorpay_payment, name='razorpay_payment'),
         path('completed-orders/', views.completed_orders, name='completed_orders'),
     path('vendor_profile/edit_vendor_details/', views.edit_vendor_details, name='edit_vendor_details'),

    path('products/', views.view_products, name='view_products'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<int:pk>/edit/', views.edit_product, name='edit_product'),
     path('products_users.html', views.products_users, name='products_users'),
     path('product/<int:pk>/', views.user_productdetails, name='user_productdetails'),
      path('categories/', views.category_list, name='category_list'),
    path('add_category/', views.add_category, name='add_category'),
     path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
     path('product_list/', views.product_list, name='product_list'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
    path('remove_product/<int:product_id>/', views.remove_product, name='remove_product'),
     path('stock_details/<int:pk>/', views.view_stock_details, name='stock_details'),
      path('restock_product/<int:pk>/', views.restock_product, name='restock_product'),
     #path('product/<int:pk>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
      #path('view_cart/', views.view_cart, name='view_cart'),
   # path('remove_from_cart/<int:cart_entry_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('buy_now/<int:pk>/', views.buy_now, name='buy_now'),
    #path('update_cart_entry/<int:cart_entry_id>/', views.update_cart_entry, name='update_cart_entry'),
#path('add_delivery_address/<int:pk>/', views.add_delivery_address, name='add_delivery_address'),
     path('add_delivery_address/', views.add_delivery_address, name='add_delivery_address'),
      path('user_delivery_address/', views.user_delivery_address, name='user_delivery_address'),
 path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('cart/', views.view_cart, name='cart'),
    path('increase-cart-item/<int:product_id>/', views.increase_cart_item, name='increase-cart-item'),
    path('decrease-cart-item/<int:product_id>/', views.decrease_cart_item, name='decrease-cart-item'),
     path('fetch-cart-count/', views.fetch_cart_count, name='fetch-cart-count'),
     
    path('create-order/', views.create_order, name='create-order'),
    path('handle-payment/', views.handle_payment, name='handle-payment'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('update_address/', views.update_address, name='update_address'),
    path('update-delivery-address/', views.update_delivery_address_page, name='update_delivery_address_page'),
    path('update-delivery-address/update/', views.update_delivery_address, name='update_delivery_address'),
    path('add_delivery_boy/', views.add_delivery_boy, name='add_delivery_boy'),
     path('add_delivery_boy_address/', views.add_delivery_boy_address, name='add_delivery_boy_address'),
     path('delivery_boy_address/', views.delivery_boy_address, name='delivery_boy_address'),
      path('order_status/', views.order_status, name='order_status'),
]



    
