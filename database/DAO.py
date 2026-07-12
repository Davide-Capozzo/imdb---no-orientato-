from database.DB_connect import DBConnect
from model.actor import Actor
from model.arco import Arco


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

    @staticmethod
    def getAllActors(rating1, rating2):#cioè i nodi del mio graph
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct n.id, n.name, n.date_of_birth 
                        from names n, role_mapping rm, movie m, ratings r  
                        where r.movie_id = m.id
                        and m.id = rm.movie_id 
                        and rm.name_id = n.id
                        and r.avg_rating between %s and %s
                        and n.date_of_birth is not NULL
                        AND (rm.category = 'actor' OR rm.category = 'actress')
                        """
            cursor.execute(query, (rating1, rating2))
            for row in cursor:
                result.append(Actor(row["id"], row["name"], row["date_of_birth"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getAllEdges(rating1, rating2):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT rm1.name_id as id1, rm2.name_id as id2,
                    SUM(CAST(replace(m.worlwide_gross_income, '$ ', '') as SIGNED)) as peso
                    FROM movie m, role_mapping rm1, role_mapping rm2, ratings r 
                    WHERE rm1.movie_id = m.id 
                    AND rm2.movie_id = m.id 
                    AND m.id = r.movie_id 
                    AND rm1.name_id < rm2.name_id 
                    AND r.avg_rating BETWEEN %s AND %s
                    AND m.worlwide_gross_income is not NULL
                    AND (rm1.category = 'actor' OR rm1.category = 'actress')
                    AND (rm2.category = 'actor' OR rm2.category = 'actress')
                    GROUP BY rm1.name_id, rm2.name_id"""

            cursor.execute(query, (rating1, rating2,))
            for row in cursor:
                result.append(Arco(row["id1"], row["id2"], row["peso"]))
            cursor.close()
            cnx.close()
        return result


