from currentStateOfAffairs.affair.affair.createDealAfterRegistration import CreateDealAfterRegistration



def createAfterRegistrationTask(id, user):
    deal = CreateDealAfterRegistration(id=id, user=user).create()
