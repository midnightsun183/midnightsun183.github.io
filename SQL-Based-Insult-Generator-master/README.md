InsultGenerator
===============

SQL and php based website which generates insults from a dictionary with parts of speech. Allows ratings of word-sentence combinations for future use.

Files Included: 
  Dictionary.txt: Dictionary of words. Included are parts of speech. (verb, noun, etc)  
  
  dictreader.py: Once a SQL database has been created and is hosted locally, dictreader.py will import every word from the 
                 dictionary file into the database.
  
  phrase generator.php: Loading this file, when the SQL database is hosted at the correct location (take a glance at the 
                        sqlconnector in the .php file to view/change location) will spit out random insults based on the parts of
                        speech in the database, with several pre-defined sentences, much like mad-libs. The sentences are also 
                        located in the database, and will need to be defined.
                  

                        
  
