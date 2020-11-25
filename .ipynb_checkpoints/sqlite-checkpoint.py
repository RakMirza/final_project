import sqlite3
def database():
    conn_obj = sqlite3.connect('sqlite3_customer.db')
    cursor = conn_obj.cursor()
    # create table customer
    create_table = " CREATE TABLE customer( name  varchar(255), address  varchar(255) ,email varchar( 255),company varchar(255), outstanding_invoices  int)"
    cursor.execute(create_table)
    conn_obj.close()

if  __name__ =='__main__':
    database()
