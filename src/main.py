
# -*- coding: utf-8 -*-

from words_db import Words_database
import re
import os.path
import time
from collections import Counter
import logging

logging.basicConfig(level=logging.DEBUG)

class TextParser:
    def __init__(self, words_db):
        self.words_db = words_db
        
    def parse_text(self, source_name, text):
        words = self.__get_words(text)
        words_count = Counter(words)
        for word in words_count: 
            logging.debug("Adding word %s %d" % (word, words_count[word]))
            self.words_db.add_word(word.lower(), source_name, count = words_count[word])

        self.words_db.apply()
        
    def __get_words(self, text):
        return re.compile('[\w\']+', re.UNICODE).findall(text.decode("utf-8"))
                
class FileParser(TextParser):
    def __init__(self, words_db):
        TextParser.__init__(self, words_db)
        
    def parse_file(self, file_path, source_name = None):
        if not os.path.isfile(file_path):
            logging.warn("Didn't find file: " + file_path)
            return None
        
        logging.info("Parsing file: " + file_path)
        
        if source_name == None:
            source_name = file_path
        
        with open(file_path, 'r') as f:
            # optimization: parse the whole file at once, not line by line
            text = f.read()
            TextParser.parse_text(self, source_name, text)
            # one by line version
            #for line in text:
            #    TextParser.parse_text(self, source_name, line)
                
class DirectoryParser(FileParser):
    def __init__(self, words_db):
        FileParser.__init__(self, words_db)
        
    def parse_dir(self, dir_path, source_name = None, files_extension = None, recursively = True):
        if recursively:
            for root, directories, filenames in os.walk(dir_path):
                for filename in filenames: 
                    file_path = os.path.join(root,filename)
                    if (files_extension == None or file_path.endswith("." + files_extension)):
                        FileParser.parse_file(self, file_path, source_name)                                    
        else:
            #TODO
            assert(False)                     
                
        
words_db = Words_database()
parser = DirectoryParser(words_db)

start = time.time()
parser.parse_dir("/home/areliga/dev/words_samples/", files_extension="txt")
logging.info("Took: " + str(time.time() - start))
