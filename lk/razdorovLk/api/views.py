import logging

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GedIdDealSerializer
from currentStateOfAffairs.utils import UtilsMethods
from currentStateOfAffairs.affair.employees.employees import WorkingWithEmployees
from .deal.updateDeal import UpdateDealAPI

logger = logging.getLogger('site')

class UpdateDeal(APIView):
    """ Обновление сделки """

    def post(self, request):
        serializer = GedIdDealSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        update = UpdateDealAPI().checkAndUpdate(idDeal=request.data['idDeal'])
        return Response('ok!')

