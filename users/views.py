from django.http import JsonResponse
from django.views import View

from users.models import ApplyDetail

import json

# Create your views here.
class ApplyJobView(View):
    def post(self, request):
        data              = json.loads(request.body)
        user, created = ApplyDetail.objects.get_or_create(
            user_id = data['user_id'],
            recruit_id = data['recruit_id']
        )

        if created == False:
            return JsonResponse({'message' : 'ALREADY_APPLIED'}, status=400)

        return JsonResponse({'message' : 'SUCCESS'}, safe=False, status=201)