from database.DB_connect import DBConnect
from model.airport import Airport

class DAO():
    @staticmethod
    def get_aereoporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"

        cursor.execute(query, ())

        for row in cursor:
            result.append(Airport(row["ID"], row["IATA_CODE"], row["AIRPORT"], row["CITY"], row["STATE"], row["COUNTRY"], row["LATITUDE"], row["LONGITUDE"], row["TIMEZONE_OFFSET"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_collegamenti(distanza_min):
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """SELECT ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID, AVG(DISTANCE) as D, COUNT(DISTANCE) as C FROM flights
                WHERE DISTANCE > '%s'
                GROUP BY ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID
                ORDER BY AVG(DISTANCE)"""

        cursor.execute(query, (distanza_min,))

        for row in cursor:
            result[(row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"])] = (row["D"], row["C"])

        cursor.close()
        conn.close()
        return result
