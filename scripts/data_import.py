import scripts.db_connector as db
from datetime import datetime

#today = datetime.today().strftime('%Y-%m-%d')
#dalo = db.conn()
#dalo_control = dalo.cursor()
#sql = ( "INSERT INTO dalo_stock_name (symbol, name, description, keywords, ipo_date) VALUES (%s, %s, %s, %s, %s)" )
#val = ("PYPL", "PayPal Inc", "smh", "stock", today)
#dalo_control.execute(sql, val)
#result = dalo_control.lastrowid
#if result != "":
#    print("Worked I think")
#else:
#    print("ughhh")
#dalo.commit()
#dalo_control.close()
#dalo.close()

def data_standard_insert( data ):
    db_conn = db.conn()
    dalo = db_conn.cursor()

    multi = True

    if isinstance( data, dict):
        multi = False
    elif isinstance( data, list):
        multi = True
    else:
        return False

    sql = "INSERT INTO dalo_stock_standard_data (stock_id, date, open, high, low, close, adjust_close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = data

    if multi:
        dalo.executemany(sql, val)
    else:
        dalo.execute(sql, val)

    db_conn.commit()
    print(dalo.lastrowid)
    return "Success!"
        
