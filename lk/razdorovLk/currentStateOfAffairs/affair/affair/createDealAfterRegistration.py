import logging

from currentStateOfAffairs.affair.employees.employees import WorkingWithEmployees
from integrations.bitrix.Deal import Deal
from currentStateOfAffairs.models import Affairs,StageAffairs
from currentStateOfAffairs.utils import UtilsMethods

logger = logging.getLogger('site')

class CreateDealAfterRegistration(UtilsMethods,WorkingWithEmployees):
    def __init__(self, id, user):
        self.id = id
        self.user = user

    def create(self):
        dealFromBitrix = self.getDeal()
        try:
            if dealFromBitrix:
                if self.getAffair(dealFromBitrix['ID']):
                    manager = self.getOrAdd(id=dealFromBitrix['ASSIGNED_BY_ID'])
                    support = self.getOrAdd(id=dealFromBitrix['UF_CRM_1668595139'])
                    boss = self.getOrAdd(id=dealFromBitrix['UF_CRM_1669542261'])
                    affair = Affairs.objects.create(
                        stage=StageAffairs.objects.get(stageId=dealFromBitrix['STAGE_ID']),
                        dateOfConclusion=self.dateFormatting(dealFromBitrix.get('UF_CRM_62DAB2BE1B9C0', None)),
                        depositPaymentDate=self.dateFormatting(dealFromBitrix.get('UF_CRM_1671619988', None)),
                        dateOfSendingToCourt=self.dateFormatting(dealFromBitrix.get('UF_CRM_1676966915519', None)),
                        caseNumber=dealFromBitrix.get('UF_CRM_6059A855ED8BE', None),
                        dateOfBankruptcy=self.dateFormatting(dealFromBitrix.get('UF_CRM_1674476382', None)),
                        completionDate=self.dateFormatting(dealFromBitrix.get('UF_CRM_1560238657391', None)),
                        idDeal=dealFromBitrix['ID'],
                        linkToKadArbitr=dealFromBitrix.get('UF_CRM_1686001000739', None),
                        manager=manager,
                        support=support,
                        boss=boss,
                    )
                    self.user.affair = affair
                    self.user.save()
        except Exception as e:
            logger.error(f"При попытке создать сделку в модели произошла ошибка.\nОшибка: {e}")

    def getDeal(self):
        """ Ищем дело в Битриксе """
        dealFromBitrix = Deal().get(self.id)
        if dealFromBitrix:
            return dealFromBitrix
        else:
            logger.info(f"Сделка с таким ID в Битриксе не найденa. ID сделки: {self.id}")
            return False

    def getAffair(self, id: int):
        """ Ищем дело в базе """
        affair = Affairs.objects.filter(idDeal=id)
        if affair:
            logger.info(f"Дело в моделе с таким Ид найдено: {id}")
            return False
        else:
            return True

