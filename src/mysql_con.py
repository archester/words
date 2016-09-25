import mysql.connector

class MySQL_Connection:
    # construction
    def __init__(self):
        self.con = mysql.connector.connect(user='root',
                                           host='127.0.0.1',
                                           database='words')
        # TODO: check if succeeded
        
        # commented out for optimization
        #self.con.autocommit = True
        
        
    # destruction
    def __del__(self):
        self.con.close()
        
    # execute query
    def execute_query(self, sql, params = None):
        cursor = self.con.cursor()
        try:            
            cursor.execute(sql, params)
        except (mysql.connector.errors.IntegrityError, mysql.connector.errors.DataError):
            return None
        except:
            print sql, params
            raise
        
        return cursor, cursor.lastrowid
        
    # sql should return at most single row containg single column
    def fetch_single_value(self, sql):
        cursor, id = self.execute_query(sql)
        row = cursor.fetchone()
        assert (row == None or len(row) == 1) and cursor.rowcount <= 1        
        
        return row[0] if cursor.rowcount > 0 else None
    
    def commit(self):
        self.con.commit()