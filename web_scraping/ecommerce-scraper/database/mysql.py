import pymysql.cursors

class MySQL ():

    def __init__ (self, server, database, username, password):

        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def run_sql (self, sql):
        """ Exceute sql code

        Run sql code in the current data base, and commit it
        """

        # Connect and get cursor
        connection = pymysql.connect(host=self.server,
                                    user=self.username,
                                    database=self.database,
                                    passwd=self.password,
                                    cursorclass=pymysql.cursors.DictCursor)

        cursor = connection.cursor()

        # Try to run sql
        try:
            cursor.execute (sql)
        except Exception as err:

            print (err, sql)

            return None

        # try to get returned part
        try:
            results = cursor.fetchall()
        except:
            results = None

        connection.commit()
        connection.close()
        return results
    
    def get_clean_text (text:str) -> str():
        
        chars = [";", "--", "\b", "\r", "\t", "\n", "\f", "\v", "\0"]
        for char in chars:
            text = text.replace(char, "")
        return text