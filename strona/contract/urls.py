from django.urls import path
from .views import (contract_manager, make_request,
                    offer_manager, make_offer, offer_list,
                    inbox, delete_message)


urlpatterns = [
    path('', contract_manager, name='create-contract'),
    path('apply', make_request, name='make-request'),
    path('offer-manager', offer_manager, name='offer-manager'),
    path('offer-manager/<int:id>', offer_manager, name='offer-manager'),
    path('makeoffer', make_offer, name='make-offer'),
    path('offer-list', offer_list, name='offer-list'),
    path("inbox", inbox, name='inbox'),
    path("delete-message", delete_message, name="delete-message"),
]
