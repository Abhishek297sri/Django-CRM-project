from django.urls import path
from customerapp import views
from customerapp import urls


urlpatterns=[

path('', views.home,name='home'),
# path('login/', views.login_user,name='login'),
path('logout/', views.logout_user,name='logout'),
path('register/', views.register_user,name='register'),
path('add_record/', views.add_record,name='add_record'),
path('record/<int:pk>', views.customer_record, name='record'),
path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
path('update_record/<int:pk>', views.update_record, name='update_record'),
# path('recordcu/<int:pk>', views.records_user,name='record'),

]