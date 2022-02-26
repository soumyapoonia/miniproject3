from http.client import UnimplementedFileMode
import mysql.connector
from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = ("SELECT product.product_id, product.name, product.unitm_id, product.price_per_unit, unitm.unitm_name  FROM product inner join unitm on unitm.unitm_id=product.unitm_id")

    cursor.execute(query)
    
   
    response = []
    for (product_id , name , unitm_id , price_per_unit, unitm_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name, 
            'unitm_id': unitm_id,
            'price_per_unit': price_per_unit,
            'unitm_name': unitm_name
          })
      


    return response 

def insert_new_product(connection, product):
    cursor = connection.cursor()

    query = ("insert into product (name, unitm_id, price_per_unit) VALUES (%s, %s, %s) ")
    
    data = (product['name'], product['unitm_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM product where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

    

if __name__=='__main__':
    connection = get_sql_connection()
    print(insert_new_product(connection,{
        'name':'cream',
        'unitm_id':'1',
        'price_per_unit':'42'
    }))