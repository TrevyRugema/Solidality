from .models import *
from .logic import *
def cycle_processor(request):
    today = today = datetime.now()
    if Cycle.objects.filter(is_active=True).exists():
        currentCycle = Cycle.objects.get(is_active=True)
    else:
        currentCycle='2021/2022'

    context = {
        'currentCycle': currentCycle,
        'today':today

    }
    return context