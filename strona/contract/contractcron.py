#!/home/viktor/PROJEKT1/venv/bin/python

from contract.models import Contract 
from datetime import datetime, timedelta
def contract_cron_job():
    contracts = Contract.objects.all()
    for contract in contracts:
        if (contract.offer.deadline > datetime.now() and
            contract.offer.deadline < datetime.now()+timedelta(days=3)):
            contract.status = "rejected"
            contract.save()
        elif (contract.offer.deadline > datetime.now()+timedelta(days=3)):
            contract.delete()
