# Her har vi hjelpefunksjoner for å jobbe mot mysql databaser.
# Imports:
import mysql.connector
from mysql.connector import Error
from typing import Optional, Tuple, List, Dict, Any, Sequence
# Functions
"""
Hva trenger vi for å opprette en connection:
host: localhost
user: root
password: gokstad
database: world
"""
def create_connection(host: str, user: str, password: str, database:str):
    """
    Denne funksjonen tar inn db connection parametere og returnerer en mysql connection
    :param host: database hoste - for oss localhost
    :param user: bruker som skal opprette en connection - for oss root
    :param password: passordet til brukeren - for oss gokstad
    :param database: hvilken database du skal jobbe mot - for oss nå world
    :return: enten MySQLConnection eller None
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print(f"Koblet til MySQL database: {database}")
            return connection
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return None

def close_connection(connection):
    """
    Lukker databaseforbindelsen

    :param connection:  MySQL connection-objekt
    """
    if connection and connection.is_connected():
        connection.close()
        print("Database-fordbindelsen er lukket")

def execute_select_dict(connection, query: str, params: Tuple = None) -> List[Dict[str, Any]]:
    """
    Gjør en SELECT query og returnerer resultatene som dictionaries.
    :param connection: MySQL connection-objekt
    :param query: SELECT query
    :param params: Parametere for prepared statemnt (valgfritt)
    :return: Lise med dictionaries (kolonnenavn: verdi)
    """
    cursor = connection.cursor(dictionary=True)
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        print(f"Querien returnerte {len(result)} rad(er).")
        return result
    except Error as e:
        print(f"Feil ved SELECT query {e}")
        return []
    finally:
        cursor.close()
