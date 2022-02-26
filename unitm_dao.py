def get_unitms(connection):
    cursor = connection.cursor()
    query = ("select * from unitm")
    cursor.execute(query)
    response = []
    for (unitm_id, unitm_name) in cursor:
        response.append({
            'unitm_id': unitm_id,
            'unitm_name': unitm_name
        })
    return response


if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_unitms(connection))