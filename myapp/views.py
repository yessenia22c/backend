from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from myapp.utils.queensAttack import queensAttack

@csrf_exempt
def queens_attack(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        n = data.get('n')
        k = data.get('k')
        rq = data.get('rq')
        cq = data.get('cq')
        obstacles = data.get('obstacles', [])

        result = queensAttack(n, k, rq, cq, obstacles)
        return JsonResponse({'attackable_squares': result})