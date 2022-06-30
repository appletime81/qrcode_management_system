# # import mysql.connector
# import mysql.connector
#
#
# # Connect to database
# def connect_db():
#     # Connect to database
#     mydb = mysql.connector.connect(
#         host="192.168.1.199",
#         user="apple",
#         passwd="",
#         database="factory_file_management",
#     )
#     return mydb
#
#
# # Get data from database
# def get_data(mydb):
#     # Get data from database
#     mycursor = mydb.cursor()
#     mycursor.execute("""SELECT * FROM file_management""")
#     myresult = mycursor.fetchall()
#     return myresult
#
#
# if __name__ == "__main__":
#     mydb = connect_db()
#     myresult = get_data(mydb)
#     print(myresult)
import datetime

a = [{'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '3000355030.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '3000355030.step',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '3000355030組合件.mp4',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '3000355030組合件.SLDASM',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '3000355030組合件A.mp4',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '3000355030組合件工程圖.SLDDRW',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '31.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '34.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '37-0.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '37-1.DWG',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '37-1.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '37-2.DWG',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '37-2.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '37-3.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '37-4.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '37-5.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '37-6.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '37.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '39.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '40.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '43--52.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '46-1.DWG',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '46-1.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '46-2.DWG',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '46-2.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '55.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '56.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '58.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '61.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '62.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': 'M5x10高長桿螺帽.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': 'M6長桿螺帽.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': 'plot.log',
      'data_insert_date': datetime.date(2022, 6, 29)},
     {'server_ip': '192.168.1.199', 'root_path': 'Database', 'file_name': '零件1.SLDPRT',
      'data_insert_date': datetime.date(2022, 6, 29)}]
print(len(a))