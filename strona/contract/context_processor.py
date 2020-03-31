from .models import Message

def new_messages(request):
    return {"new_messages_amount": Message.objects.filter(to=request.user).count()}
