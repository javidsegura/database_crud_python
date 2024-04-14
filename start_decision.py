import os,time

import read_mode, load_csv, write_mode

def give_greetings():

      """
      
            Description: This function is going to display the homepage of the database management system. 
            It is going to display the project schema and the user is going to be able to select an option.

      """

      os.system("clear")
      
      # 1. Call header element
      header("homepage/")

      #2. Display project schema
      print("\n\n Project Schema: ")
      print("-"*30)
      print("|\n|")
      print("|---> READ \t\t(1)")
      print("  |")
      print("  |->Full database \t(1.1)")
      print("  |->Categories \t(1.2)")
      print("  |->Conditions \t(1.3)")
      print("  |->Index \t\t(1.4)")
      print("|")
      print("|")
      print("|---> WRITE \t\t(2)")
      print("  |")
      print("  |->ADD \t\t(2.1)")
      print("    |-> COLUMN \t\t(2.1.1)")
      print("    |-> ROW \t\t(2.1.2)")
      print("  |->EDIT \t\t(2.2)")
      print("    |-> COLUMN \t\t(2.2.1)")
      print("    |-> ROW \t\t(2.2.2)")
      print("  |->DELETE \t\t(2.3)")
      print("    |-> COLUMN \t\t(2.3.1)")
      print("    |-> ROW \t\t(2.3.2)")

      print("-"*30)
      
      # 3. User input on entry mode
      print("\n(*) Select your option here: ")
      user_input = str(input("==> ")).lower()


      # 4. Read section
      if user_input == "1" or user_input == "read":
            user_input = "read"
      elif user_input == "1.1" or user_input == "full database" or user_input == "full db" or user_input == "read full database" or user_input == "read full db":
            user_input = "full_database"
      elif user_input == "1.2" or user_input == "categories" or user_input == "read categories":
            user_input = "categories"
      elif user_input == "1.3" or user_input == "conditions" or user_input == "read conditions":
            user_input = "conditions"
      elif user_input == "1.4" or user_input == "index" or user_input == "read index":
            user_input = "index"

      # 5. Write section
      elif user_input == "2" or user_input == "write":
            user_input = "write"
      elif user_input == "2.1" or user_input == "add" or user_input == "write add":
            user_input = "add"
      elif user_input == "2.1.1" or user_input == "add column" or user_input == "add col" or user_input == "add c" or user_input == "add cols" or user_input == "add columns" or user_input == "write add column" or user_input == "write add col" or user_input == "write add c" or user_input == "write add cols" or user_input == "write add column" or user_input == "write add col" or user_input == "write add c" or user_input == "write add cols": 
            user_input = "column_add"
      elif user_input == "2.1.2" or user_input == "add row" or user_input == "add r" or user_input == "add record" or user_input == "add records" or user_input == "add rows" or user_input == "write add row" or user_input == "write add r" or user_input == "write add record" or user_input == "write add records" or user_input == "write add rows":
            user_input = "row_add"
      elif user_input == "2.2" or user_input == "edit":
            user_input = "edit"
      elif user_input == "2.2.1" or user_input == "edit column" or user_input == "edit col" or user_input == "edit c" or user_input == "edit cols" or user_input == "edit columns" or user_input == "write edit column" or user_input == "write edit col" or user_input == "write edit c" or user_input == "write edit cols" or user_input == "write edit column" or user_input == "write edit col" or user_input == "write edit c" or user_input == "write edit cols":
            user_input = "column_edit"
      elif user_input == "2.2.2" or user_input == "edit row" or user_input=="edit r" or user_input == "edit record" or user_input == "edit records" or user_input == "edit rows" or user_input == "write edit row" or user_input == "write edit r" or user_input == "write edit record" or user_input == "write edit records" or user_input == "write edit rows":
            user_input = "row_edit"
      elif user_input == "2.3" or user_input == "delete" or user_input == "del" or user_input == "remove" or user_input == "rem" or user_input == "rm" or user_input == "write delete" or user_input == "write del" or user_input == "write remove" or user_input == "write rem" or user_input == "write rm" or user_input == "write delete" or user_input == "write del" or user_input == "write remove" or user_input == "write rem" or user_input == "write rm":
            user_input = "delete"
      elif user_input == "2.3.1" or user_input == "delete column" or user_input == "delete col" or user_input == "delete c" or user_input == "del column" or user_input == "del col" or user_input == "del c" or user_input == "remove column" or user_input == "remove col" or user_input == "remove c" or user_input == "rem column" or user_input == "rem col" or user_input == "rem c" or user_input == "rm column" or user_input == "rm col" or user_input == "rm c" or user_input == "write delete column" or user_input == "write delete col" or user_input == "write delete c" or user_input == "write del column" or user_input == "write del col" or user_input == "write del c" or user_input == "write remove column" or user_input == "write remove col" or user_input == "write remove c" or user_input == "write rem column" or user_input == "write rem col" or user_input == "write rem c" or user_input == "write rm column" or user_input == "write rm col" or user_input == "write rm c":
            user_input = "column_delete"
      elif user_input == "2.3.2" or user_input == "delete row" or user_input == "delete r" or user_input == "delete record" or user_input == "del row" or user_input == "del r" or user_input == "del record" or user_input == "remove row" or user_input == "remove r" or user_input == "remove record" or user_input == "rem row" or user_input == "rem r" or user_input == "rem record" or user_input == "rm row" or user_input == "rm r" or user_input == "rm record" or user_input == "write delete row" or user_input == "write delete r" or user_input == "write delete record" or user_input == "write del row" or user_input == "write del r" or user_input == "write del record" or user_input == "write remove row" or user_input == "write remove r" or user_input == "write remove record" or user_input == "write rem row" or user_input == "write rem r" or user_input == "write rem record" or user_input == "write rm row" or user_input == "write rm r" or user_input == "write rm record":
            user_input = "row_delete"

      # COMMANDS SECTION
      elif user_input == "-end":
            user_input = "-end"
      elif user_input == "-prior":
            user_input = "-prior"
      elif user_input == "-home":
            user_input = "-home"
      elif user_input == "-full":
            user_input = "-full"


      return user_input


def header(directory):

      """
      
      Description: This function is going to display the header of the database management system.

      Parameters: current directory
      
      
      """

      print()
      print("-"*200)
      print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ~COMMANDS:")
      print("\t\t\tDATABASE MANAGEMENT SYSTEM \t\t\t\t\t\t\t\t\t\t  -end => terminate session ; -prior => go to the previous menu")
      print(f"~NAVIGATION: {directory}  \t\t\t\t\t\t\t\t\t\t\t\t\t  -home=> go to the homepage ; -full => see full database")
      print("-"*200)


def command_prompting(mode,case,_input = None):

      """ 
      
      Describe: This function is going to prompt the user for a command (see options in the header).

      Parameters: 
            - mode: read, write, edit, delete
            - case: basic, back_to_greetings, back_to_subscripting --> Different cases for different situations
            - _input: input prior to calling the function that may be used to display as error message
      
      
      """

      if mode == "read":
            if case == 1:
                  flag = True
                  print("\n(*) Write a command: ")

                  while flag:
                        command = input("==> ").lower()
                        if command == "-prior": 
                              flag = False
                              read_mode.read_main() 
                              pass 
                        elif command == "-home":
                              flag = False
                              print()
                        elif command == "-end":
                              flag = False
                              end_screen()
                        elif command == "-full":
                              print("You already are in the full database.")
                              time.sleep(2)
                        else:
                              print(f"ERROR #4: Command '{command}' does not exist, please try again.\n")
                              time.sleep(2)
            else:
                  flag = True
                  print("\n(*) Write a command: ")     

                  while flag:
                        command = input("==> ").lower()

                        if command == "-prior": 
                              flag = False
                              read_mode.read_main() 
                              pass 
                        elif command == "-home":
                              flag = False
                              print()
                        elif command == "-end":
                              flag = False
                              end_screen()

                        elif command == "-full":
                              flag = False
                              load_csv.creating_datframe() # Load the CSV again, to make sure it is updated.
                              read_mode.read_complete_db()
                        else:
                             errors(4,command)


      elif mode == "write" or  mode == "edit" or mode == "delete":

            if case == "implicit": # Implicit means the user wrote a command that in some input field throughout the program.
                  if _input == "-prior":
                        pass
                  elif _input == "-home":
                        pass
                  elif _input == "-end":
                        end_screen()
                  elif _input == "-full":
                        load_csv.creating_datframe() # Load the CSV again, to make sure it is updated.
                        read_mode.read_complete_db()
                  else:
                        errors(4,_input)

            elif case == "back_to_greetings":
                  if _input == "-prior":
                        write_mode.greetings()
                  elif _input == "-home":
                        print()
                  elif _input == "-end":
                        end_screen()
                  elif _input == "-full":
                        load_csv.creating_datframe() # Load the CSV again, to make sure it is updated.
                        read_mode.read_complete_db()
                  else:
                        errors(4,_input)

            elif case == "back_to_subscripting":
                  if _input == "-prior":
                        read_mode.read_index(mode)
                  elif _input == "-home":
                        print()
                  elif _input == "-end":
                        end_screen()
                  elif _input == "-full":
                        load_csv.creating_datframe()
                        read_mode.read_complete_db()
                  else:
                        errors(4,_input)

                              


def end_screen(): 

      """
      
      Description: This function is going to display a goodbye message and terminate the session.
      
      """


      os.system("clear")
      print("Goodbye!")
      time.sleep(1)
      exit(1)


def errors(number, input = ""):

      """
      
      Description: This function is going to display an error message based on the number of the error.

      Parameters: 
            - number: error number
            - input: input that caused the error

      """


      if number == 1:
            print(f"ERROR #1: Your input '{input}' is not an option, please try again.")

      elif number ==2:
            print(f"ERROR #2: Column {input} does not exist, please try again.")

      elif number == 3:
            print(f"ERROR #3: Index {input} out of bound, please try again.")

      elif number == 4:
            print(f"ERROR #4: Command '{input}' does not exist, please try again.")
            
      time.sleep(2)