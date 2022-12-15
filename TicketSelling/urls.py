"""TicketSelling URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/', include(('reservation.urls', 'reservation'), namespace='reservation')),
    path('payment/', include(('payment.urls', 'payment'), namespace='payment')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('', include(('event.urls', 'event'), namespace='event')),
]
