import helper_db as db
CONNECTION_DATA = {
        "host": "localhost",
        "user": "root",
        "password": "gokstad",
        "database": "world"
    }
#conn = db.create_connection(host="localhost", user="root", password="gokstad", database="world")

def main():
    conn = db.create_connection(**CONNECTION_DATA)

    if not conn:
        print("Kunne ikke koble til databasen")
        return

    try:
        parameter = ("NOR",)
        first_query = "SELECT * FROM city WHERE CountryCode = %s"
        first_result = db.execute_select_dict(conn, first_query, parameter)

        print(first_result)

        for result in first_result:
            print(result)
    except Exception as e:
        print(f"En feil oppstod: {e}")

    finally:
        db.close_connection(conn)

if __name__ == "__main__":
    main()