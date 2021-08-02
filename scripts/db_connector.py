import mysql.connector
from mysql.connector import errorcode

def conn():
    config = {
            'user': 'dalo_site',
            'password': 'L0L!mFck3d',
            'host': '18.218.239.62',
            'database': 'dalo_db',
            'raise_on_warnings': True
    }

    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        return("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        return("Database does not exist")
      else:
        return(err)
    return cnx
