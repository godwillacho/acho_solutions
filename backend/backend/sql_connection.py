import mysql.connector

## this is the  file where the mysql connnection is created .
__cnx = None
def get_sqlconnection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root',password='Anahita123',host='127.0.0.1',database='acho_solutions')
       
    return __cnx
