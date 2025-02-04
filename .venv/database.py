import psycopg2

class Database:
    #Коннектимся к Бд
    def __init__(self):
        self.conn = psycopg2.connect(dbname = "example",
                                     user = "postgres",
                                     password = "0000",
                                     host = "localhost",
                                     port = "5432")
        self.cursor = self.conn.cursor()


    def add_user(self,name,password,role):

       try:
           self.cursor.execute("INSERT INTO users(name,password,role) VALUES(%s,%s,%s)",(name,password,role))

           self.conn.commit()

           return True
       except psycopg2.IntegrityError:
           self.conn.rollback()
           return False


    def get_user(self,name,password):
        self.cursor.execute("SELECT name,role FROM users WHERE name = %s AND password = %s",(name,password))

        return self.cursor.fetchone()



    def close(self):
        self.cursor.close()
        self.conn.close()
