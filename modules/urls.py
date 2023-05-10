from django.urls import path, include
from modules import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('logout/', views.logout, name="logout"),
    path('giver_register/' , views.giver_register, name= 'giver_register'),
    path('taker_register/', views.taker_register, name='taker_register'),
    path('login/', views.login, name='login'),
    path('giver_home/', views.giver_home, name='giver_home'),
    path('taker_home/', views.taker_home, name='taker_home'),
    path('make_trip/', views.make_trip, name='make_trip'),
    path('trip_details/', views.trip_details, name='trip_details'),
    path('available_trip/', views.available_trip, name='available_trip'),
    path('request_trip/<str:taker_name>/<str:giver_name>/<str:date>/<str:veh_model>/<str:start>/<str:dest>/<str:trip_id>', views.request_trip, name='request_trip'),
    path('acceptance/', views.acceptance, name='acceptance'),
    path('request_trips/' , views.request_trips, name="request_trips"),
    path('accept_trip/<str:trip_id>/<str:id>',views.accept_trip, name="accept_trip"),
    path('redirect/<str:trip_id>', views.redirects, name="redirects"),
    path('payment_card/<str:id>', views.payment_card, name="payment_card"),
    path('payment_processing/<str:id>', views.payment_processing, name="payment_processing"),
    path('payment_completion/<str:id>/<str:trans_id>', views.payment_completion, name="payment_completion"),
    path('receipt/<str:id>/<str:trans_id>', views.receipt, name="receipt"),
    path('receipt_view/', views.receipt_view, name="receipt_view"),
    path('receipt_info/<str:pay_id>/<str:trip_id>', views.receipt_info, name="receipt_info"),
    path('giver_receipt_view/<str:trip_id>', views.giver_receipt_view, name="giver_receipt_view"),
    path('test/', views.test, name="test"),
]
