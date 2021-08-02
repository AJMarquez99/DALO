import scripts.db_connector as db

def get_symbol_id( sym ):
    sql = "SELECT id FROM dalo_stock_name WHERE symbol = '" + sym + "' LIMIT 1;"

    db_conn = db.conn()
    dalo = db_conn.cursor(dictionary=True)

    dalo.execute(sql)
    result = dalo.fetchone()
    if result == None:
        return False
    else:
        return result['id']

def get_values( sym, col):
    sym_id = str(get_symbol_id( sym ))
    sql = "SELECT " + col + " FROM dalo_stock_standard_data WHERE stock_id = " + sym_id + ";"

    db_conn = db.conn()
    dalo = db_conn.cursor(dictionary=True)

    dalo.execute(sql)

    result = dalo.fetchall()

    result_list = []
    for row in result:
        result_list.append( row[col] )

    return result_list

#data = get_values( "SNAP", "date" )
#for row in data:
#    print(row["date"])
