from pontaj.models import Pontaj


def is_ready_to_work(request):
    if request.user.is_authenticated:
        if Pontaj.objects.filter(user_id=request.user.id, end_date=None).exists():
            return {'ready': False}
        return {"ready": True}
    return {}
