# import mysql.connector
import mysql.connector


# Connect to database
def connect_db():
    # Connect to database
    mydb = mysql.connector.connect(
        host="192.168.1.199",
        user="apple",
        passwd="",
        database="factory_file_management",
    )
    return mydb


# Get data from database
def get_data(mydb):
    # Get data from database
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT * FROM file_management""")
    myresult = mycursor.fetchall()
    return myresult


if __name__ == "__main__":
    mydb = connect_db()
    myresult = get_data(mydb)
    print(myresult)
