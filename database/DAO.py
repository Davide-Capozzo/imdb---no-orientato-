from database.DB_connect import DBConnect

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getRangeRatings():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct avg_rating
                        from ratings r 
                        group by avg_rating 
                        order by avg_rating asc
                        """
            cursor.execute(query)
            for row in cursor:
                result.append(row["avg_rating"])
            cursor.close()
            cnx.close()
        return result




