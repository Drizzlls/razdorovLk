from datetime import datetime



class UtilsMethods:
    @staticmethod
    def dateFormatting(date):
        """ Преобразование даты """
        if date:
            return date[0:10]
        else:
            return None