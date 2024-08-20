from currentStateOfAffairs.affair.employees.employees import WorkingWithEmployees
from currentStateOfAffairs.utils import UtilsMethods
from currentStateOfAffairs.models import Affairs, StageAffairs
from integrations.bitrix.Deal import Deal
from typing import Any, Dict


class UpdateDealAPI(UtilsMethods, WorkingWithEmployees):

    def getDealFromModel(self, idDeal: int) -> bool:
        """
        Поиск сделки в Моделе Affairs. Возвращает True или False. Взависимости от того, есть ли ид в базе или нет.
        @param idDeal: ид сделки
        @type idDeal: int
        @return: Bool
        """
        return Affairs.objects.filter(idDeal=idDeal).exists()

    def getDealFromBitrix(self, idDeal: int) -> dict[str, Any] | bool:
        """
        Получение сделки из Битрикс24
        @param idDeal: Ид сделки
        @type idDeal: int
        @return: Dict
        """
        return Deal().get(id=idDeal)

    def updateAffair(self, idDeal: int, data: dict) -> bool:
        #FIXME: Сделать класс для обновления,чтобы избежать повторения кода
        try:
            affair = Affairs.objects.filter(idDeal=idDeal).update(
                stage=StageAffairs.objects.get(stageId=data['STAGE_ID']),
                dateOfConclusion=self.dateFormatting(data.get('UF_CRM_62DAB2BE1B9C0', None)),
                depositPaymentDate=self.dateFormatting(data.get('UF_CRM_1671619988', None)),
                dateOfSendingToCourt=self.dateFormatting(data.get('UF_CRM_1676966915519', None)),
                caseNumber=data.get('UF_CRM_6059A855ED8BE', None),
                dateOfBankruptcy=self.dateFormatting(data.get('UF_CRM_1674476382', None)),
                completionDate=self.dateFormatting(data.get('UF_CRM_1560238657391', None)),
                linkToKadArbitr=data.get('UF_CRM_1686001000739', None),
                manager=self.getOrAdd(id=data['ASSIGNED_BY_ID']),
                support=self.getOrAdd(id=data['UF_CRM_1668595139']),
                boss=self.getOrAdd(id=data['UF_CRM_1669542261']),
            )
            return True
        except:
            return False

    def checkAndUpdate(self, idDeal: int) -> bool:
        """
        Получаем ид сделки из запроса. Проверяем, есть ли в базе. Если есть, то ищем в Битриксе. Если и там есть данные,
        но обновляем данные в базе
        @param idDeal: Ид сделки
        @type idDeal: int
        @return: Bool
        """
        deal = self.getDealFromModel(idDeal)
        if deal and (dealBitrix := self.getDealFromBitrix(idDeal)):
            self.updateAffair(idDeal, dealBitrix)
            return True
        else:
            return False
