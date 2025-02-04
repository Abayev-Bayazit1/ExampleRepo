from database import Database
from system import System


class Starter:
    def __init__(self):
        self.db = Database()
        self.system = System(self.db)


    def start(self):


        while True:
            print("\n[1].Login ")
            print("[2].Register ")
            print("[3].Exit")

            try:
                choise = int(input("Enter your choice : "))

            except ValueError:
                print("\n Choice should be an integer")
                continue

            if choise == 1:
                self.system.login()


            elif choise == 2:
                self.system.register()


            elif choise == 3:
                print("Exitting from the application...")
                self.db.close()
                break

            else:
                print("Invalid choice")
