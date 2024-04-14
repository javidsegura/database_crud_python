
# LIBRARIES
import pandas, time


#MODULES
import load_csv as load_csv 
import start_decision
import read_mode 
import write_mode



# HOMEPAGE CODE

def homepage():


      while True:
            
            # 0. Start Screen
            user_homepage_option = start_decision.give_greetings()
            
            # 1. Load CSV every loop in the while loop
            load_csv.creating_datframe()

            # 2. Commands Section
            if user_homepage_option == "-end":
                        start_decision.end_screen()
            elif user_homepage_option == "-prior":
                        pass
            elif user_homepage_option == "-home":
                        print("You are already at the homepage.")
                        time.sleep(2)
                        pass 
            elif user_homepage_option == "-full":
                        read_mode.read_complete_db()
          

             # 3. Set up entry modes
            elif user_homepage_option == "read": # 1 - Read
                        read_mode.read_main()
            elif user_homepage_option == "full_database":  # 1.1 - Read Full Database
                        read_mode.read_complete_db() 
            elif user_homepage_option == "categories": # 1.2 - Read by Categories
                        read_mode.read_categories()
            elif user_homepage_option == "conditions": # 1.3 - Read by Conditions
                        read_mode.read_conditions("read")
            elif user_homepage_option == "index": # 1.4 - Read by Index
                        read_mode.read_index("read")
                  
            elif user_homepage_option == "write": # 2 - Write
                        write_mode.write_main()
            elif user_homepage_option == "add": # 2.1 - Add
                        write_mode.colum_or_row("add")
            elif user_homepage_option == "column_add": # 2.1.1 - Add Column
                        write_mode.colum_or_row("add", "column")
            elif user_homepage_option == "row_add": # 2.1.2 - Add Row
                        write_mode.colum_or_row("add", "row")
            elif user_homepage_option == "edit": # 2.2 - Edit
                        write_mode.colum_or_row("edit") 
            elif user_homepage_option == "column_edit": # 2.2.1 - Edit Column
                        write_mode.colum_or_row("edit", "column")
            elif user_homepage_option == "row_edit": # 2.2.2 - Edit Row
                        write_mode.colum_or_row("edit", "row")
            elif user_homepage_option == "delete": # 2.3 - Delete
                        write_mode.colum_or_row("delete")
            elif user_homepage_option == "column_delete":  # 2.3.1 - Delete Column
                        write_mode.colum_or_row("delete", "column")
            elif user_homepage_option == "row_delete": # 2.3.2 - Delete Row
                        write_mode.colum_or_row("delete", "row")
            else:
                        # 4. Error Handling
                        start_decision.errors(1, user_homepage_option)
                        




if __name__ == "__main__":
      homepage()
