from mysql_con import MySQL_Connection

class Words_database:
    
    def __init__(self):
        self.db_con = MySQL_Connection()
    
    def add_word(self, word, source = None, count = 1):
        #word_id = self.__word_id(word)
        #if (word_id == None):
        word_id = self.__add_word(word)
            
        if source != None:
            #source_id = self.__source_id(source)
            #if (source_id == None):
            source_id = self.__add_source(source)
              
            if word_id == None or source_id == None:
                print "Word  = " + word + " source = " + source
            
            return self.__inc_word_in_source(word_id, source_id, count)
        
    def apply(self):
        self.db_con.commit()            
                                
     
    def __add_word(self, word):
        query = "insert into words(word) values (%s) on duplicate key update id = id"
        unused, id = self.db_con.execute_query(query, (word,))
        assert (id != None)
        return id
    
    def __add_source(self, source):
        query = "insert into sources(source) values(%s) on duplicate key update id = id"
        unused, id = self.db_con.execute_query(query, (source,))
        assert (id != None)
        return id

#     def __source_id(self, source):
#         query = "select id from sources where source = " + self.__quote(source)
#         return self.db_con.fetch_single_value(query)
#         
#     def __word_id(self, word):
#         query = "select id from words where word = " + self.__quote(word)
#         return self.db_con.fetch_single_value(query)
    
    def __inc_word_in_source(self, word_id, source_id, count):        
        query = "insert into words_instances(word_id, source_id, count) values " \
                 + "(%s, %s, %s) on duplicate key update count = count + %s"
        params = (word_id, source_id, count, count)
            
        return self.db_con.execute_query(query, params)
