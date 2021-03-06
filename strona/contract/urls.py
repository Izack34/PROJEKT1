from django.urls import path
from .views import (contract_manager, make_request,
                    offer_manager, make_offer, offer_list,
                    inbox, delete_message, inbox_notification,
                    contract_list, contract_detail, make_complain,
                    contract_processing, contract_download)


urlpatterns = [
    path('', contract_manager, name='create-contract'),
    path('apply', make_request, name='make-request'),
    path('offer-manager', offer_manager, name='offer-manager'),
    path('offer-manager/<int:id>', offer_manager, name='offer-manager'),
    path('makeoffer', make_offer, name='make-offer'),
    path('offer-list', offer_list, name='offer-list'),
    path("inbox", inbox, name='inbox'),
    path("delete-message", delete_message, name="delete-message"),
    path("inbox-notification", inbox_notification, name="inbox-notification"),
    path("contract-list", contract_list, name='contract-list'),
    path("contract-detail/<int:id>", contract_detail, name='contract-detail'),
    path("contract-processing/<int:id>", contract_processing, name='contract-processing'),
    path("contract-download/<path:filename>", contract_download, name='contract-download'),
    path("make-complain/<int:id>", make_complain, name='make-complain'),
]
