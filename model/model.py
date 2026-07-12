from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def getRatings(self):
        return DAO.getRangeRatings()