from django.http import JsonResponse
from django.views import View

from .models import Recruit

import json

class RecruitView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            Recruit.objects.create(
                company_id = data['company_id'],
                position_id = data['position_id'],
                compensation = data['compensation'],
                content = data['content'],
                stack_id = data['stack_id'] 
            )

            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError :
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)