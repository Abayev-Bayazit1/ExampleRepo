from database import Database



class System:
    def __init__(self,db):
        self.db = db

    def login(self):
        print("\nEnter username and password")
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        user  = self.db.get_user(name,password)

        if user:
            print(f"Login completed! Welcome,{user[0]}.Your role is {user[1]}")

            if user[1] == "admin":
                self.admin_menu()
            else:
                print("smth")

        else:
            print("Login failed")


    def register(self):
        print("\nEnter your login details")

        try:
            name = input("Enter your name : ")
            password = input("Enter your password : ")
            role =input("Enter your role : ")

            if self.db.add_user(name,password,role):
                print("✅ Registered successfully")
            else:
                print("❌ User already exists" )

        except ValueError:
            print("\nEnter correct login details")

    def view_all_users(self):
       users =  self.db.view_all_users()

       if not users:
           print("No users registered")

       print("\nUsers:")
       for user in users:
           print(f"🆔 {user[0]} | 👤 {user[1]} | 🎭 Role: {user[2]}")


    def delete_user(self):
        name = input("Enter name for delete: ")

        try:
            if self.db.delete_user(name):
                print("Deleted user")

            else:
                print("User not found")

        except ValueError:
            print("Error with deleting user..")



    def admin_menu(self):
        while True:
            print("[1].View all registered users")
            print("[2].Delete registered users")
            print("[3].Back")


            try:
                choise = int(input("Enter your choice : "))
            except ValueError:
                print("Choise must be an integer")
                continue

            if choise == 1:
                self.view_all_users()

            elif choise == 2:
                self.delete_user()

            elif choise == 3:
                print("🔙 Backing...")
                break

            else:
                print("❌ Invalid choice")
