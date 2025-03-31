from sql_connection import get_sqlconnection


def display_all_products(connection):
    cursor = connection.cursor()

    query = ("SELECT product_table.product_id, product_table.product_name, product_table.unit_id ,product_table.Product_name , product_table.exp_date , product_table.unit_cost_price ,"
    " product_table.unit_selling_price, product_table.stock_quantity, unit.unit_name FROM product_table inner join unit on product_table.unit_id=unit.unit_id")

    cursor.execute(query)

    response =[]

    for (product_id, product_name, unit_id, product_name_dup, exp_date, unit_cost_price, unit_selling_price, stock_quantity, unit_name) in cursor:
        response.append({
            'product_id': product_id,
            'product_name': product_name,
            'exp_date': exp_date,
            'stock_quantity': stock_quantity,
            'unit_name': unit_name,
            'unit_cost_price': unit_cost_price,
            'unit_selling_price': unit_selling_price,})
    return response 
def insert_new_product(connection, product_table):
    cursor = connection.cursor()
    query =  ("INSERT INTO product_table "
              "(product_name,exp_date,unit_cost_price,unit_selling_price,stock_quantity,unit_id,)"
              "VALUES(%s,%s,%s,%s,%s,%s)")\
              
    data = (product_table['product_name'],product_table['unit_id'],product_table['stock_quantity'],product_table['eexp_date'],
            product_table['unit_cost_price'],product_table['unit_selling_price'])
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
    print(display_all_prtoducts(connection)) 