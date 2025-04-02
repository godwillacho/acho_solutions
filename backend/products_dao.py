from  sql_connection import get_sqlconnection


def display_all_products(connection):
    cursor = connection.cursor()

    query = ("SELECT product.product_id, product.product_name, product.unit_id , product.exp_date , product.picture,"
     "product.price, product.quantity, unit.unit_name FROM product inner join unit on product.unit_id=unit.unit_id;")

    cursor.execute(query)

    response =[]

    for (product_id, product_name, unit_id,  exp_date,picture,price,quantity, unit_name) in cursor:
        response.append({
            'product_id': product_id,
            'product_name': product_name,
            'exp_date': exp_date,
            'quantity': quantity,
            'unit_name': unit_name,
            'price': price,
            'picture': picture})
    return response 
def insert_new_product(connection, product_table):
    cursor = connection.cursor()
    query =  ("INSERT INTO product_table "
              "(product_name,exp_date,price,picture,quantity,unit_id,)"
              "VALUES(%s,%s,%s,%s,%s,%s)")\
              
    data = (product_table['product_name'],product_table['unit_id'],product_table['quantity'],product_table['exp_date'],
            product_table['picture'],product_table['price'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM product_table WHERE product_id = " + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__ == '__main__':
    connection = get_sqlconnection()
    print(display_all_products(connection)) 