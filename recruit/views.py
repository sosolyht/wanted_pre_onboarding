from django.http import JsonResponse
from django.views import View
from django.db.models import Q

from .models import Recruit

import json


class RecruitView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            Recruit.objects.create(
                company_id   = data['company_id'],
                position_id  = data['position_id'],
                compensation = data['compensation'],
                content      = data['content'],
                stack_id     = data['stack_id'] 
            )

            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

    def get(self, request):
        jobs = Recruit.objects.all()
        result = [{
            'id'           : job.id,
            'company'      : job.company.name,
            'country'      : job.company.location.country.name,
            'state'        : job.company.location.state.name,
            'position'     : job.position.name,
            'compensation' : job.compensation,
            'stack'        : job.stack.name
        }for job in jobs]

        return JsonResponse(result, safe=False, status=200)


class RecruitDetailView(View):
    def get(self, request, job_id):

        datas = Recruit.objects.filter(id=job_id)
        result = [{
            'id'           : data.id,
            'company'      : data.company.name,
            'country'      : data.company.location.country.name,
            'state'        : data.company.location.state.name,
            'position'     : data.position.name,
            'compensation' : data.compensation,
            'stack'        : data.stack.name,
            'content'      : data.content,
            'similar'      : [similar.id for similar in Recruit.objects.all()][:5]
        }for data in datas]

        return JsonResponse(result, safe=False, status=200)


class RecruitModifyView(View):
    def put(self, request, job_id):
        try:
            job = Recruit.objects.get(id=job_id)
            data = json.loads(request.body)
            job.position_id  = data['position_id']
            job.compensation = data['compensation']
            job.content      = data['content']
            job.stack_id     = data['stack_id']

            job.save()

            return JsonResponse({"message" : "SUCCESS"}, status=200)

        except Recruit.DoesNotExist:
            return JsonResponse({"message" : "DOES_NOT_EXIST"}, status=404)


    def delete(self, request, job_id):
        try:
            Recruit.objects.get(id=job_id).delete()
            return JsonResponse({"message" : "DELETE_SUCCESS"}, status=200)

        except Recruit.DoesNotExist:
            return JsonResponse({"message" : "DOES_NOT_EXIST"}, status=404)


class JobSearchView(View):
    def get(self, request):
        try:
            query = request.GET.get('query')

            results = Recruit.objects.filter(Q(company_id__name__iexact = query) | Q(stack_id__name__iexact = query))
            result = [{
                'id'           : result.id,
                'company'      : result.company.name,
                'country'      : result.company.location.country.name,
                'state'        : result.company.location.state.name,
                'position'     : result.position.name,
                'compensation' : result.compensation,
                'stack'        : result.stack.name
            }for result in results]

            return JsonResponse(result, safe=False, status=200)

        except Recruit.DoesNotExist:
            return JsonResponse({"message" : "DOES_NOT_EXIST"}, status=404)