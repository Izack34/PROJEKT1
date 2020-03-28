from django.urls import path
from .views import contract_manager, make_request


urlpatterns = [
    path('', contract_manager, name='create-contract'),
    path('apply', make_request, name='make-request'),
]
