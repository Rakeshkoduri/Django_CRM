from django.urls import path
from . import views




urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about, name='about'),

    path('register/', views.register, name='register'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout_page/', views.logout_page, name='logout_page'),

    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/',views.add_record,name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),



]
