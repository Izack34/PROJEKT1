from .models import Message

def new_messages(request):
    if request.user.is_anonymous:
        return {"new_messages_amount": 0}
    return {"new_messages_amount": Message.objects.filter(to=request.user).count()}
