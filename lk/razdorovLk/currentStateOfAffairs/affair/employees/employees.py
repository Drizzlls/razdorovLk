import logging
import pprint
from currentStateOfAffairs.models import Employees
from typing import Dict, Any
from integrations.bitrix.Employee import EmployeeFromBitrix24
logger = logging.getLogger('site')


class WorkingWithEmployees:

    def update(self):
        pass

    def addFromModel(self, data: dict) -> dict[str | Any] | bool:
        try:
            employee = Employees.objects.create(
                name=data['NAME'],
                lastName=data['LAST_NAME'],
                secondName=data.get('SECOND_NAME', ''),
                personalId=data['ID'],
                phone=data.get('WORK_PHONE', '')
            )
            employee.save()
            return employee
        except Employees as e:
            logger.critical(f"При попытке создать сотрудника произошла ошибка.\nОшибка: {e}")
            return None

    def getOrAdd(self, id: int) -> dict[str | Any]:
        employee = Employees.objects.filter(personalId=id).first()
        if employee:
            return employee
        else:
            employeeFromBitrix24 = self.getFromBitrix24(id)
            employeeModel = self.addFromModel(employeeFromBitrix24[0])
            return employeeModel

    def getFromBitrix24(self, id: int) -> dict[str | Any]:
        employeeFromBitrix24 = EmployeeFromBitrix24().get(id)
        return employeeFromBitrix24
