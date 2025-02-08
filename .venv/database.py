import psycopg2

class Database:
    #Коннектимся к БД
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

    def view_all_users(self):
        self.cursor.execute("SELECT id,name,role FROM users")
        # self.conn.commit()
        return self.cursor.fetchall()



    def delete_user(self,name):
        self.cursor.execute("DELETE FROM users WHERE name = %s",(name,))
        self.conn.commit()
        return self.cursor.rowcount > 0


    def update_user_password(self,name,password):
        self.cursor.execute("UPDATE users SET password = %s WHERE name = %s",(password,name))
        self.conn.commit()
        return self.cursor.rowcount > 0


    def update_username(self,new_username,password):
        try:
            self.cursor.execute("SELECT id FROM users WHERE password = %s",(password,))
            user = self.cursor.fetchone()

            if not user:
                print("User not found or password is incorrect")

            self.cursor.execute("UPDATE users SET name = %s WHERE password = %s",(new_username,password))
            self.conn.commit()

            return self.cursor.rowcount > 0
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return False


    def  view_generalInformation(self):
        self.cursor.execute("")
        self.conn.commit()
        return self.cursor.fetchall()


    def close(self):
        self.cursor.close()
        self.conn.close()
