#!/home/viktor/PROJEKT1/venv/bin/python

from contract.models import Contract 
from datetime import datetime, timedelta
def contract_cron_job():
    contracts = Contract.objects.all()
    for contract in contracts:
        if (contract.offer.deadline+timedelta(days=3) < datetime.now().date()):
            contract.offer.delete()
            contract.delete()
        elif (contract.offer.deadline <= datetime.now().date()):
            contract.status = "rejected"
            contract.save()
