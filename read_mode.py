import os,time

import load_csv
import write_mode
import start_decision


def read_main():
     
     # 1. Set up entry point
      user_read_mode_main_option = greetings()

      # 2. Select modes
      if user_read_mode_main_option == "read_complete_db":
            read_complete_db()

      elif user_read_mode_main_option == "read_categories":
            read_categories()

      elif user_read_mode_main_option == "read_conditions":
            read_conditions("read")
      
      elif user_read_mode_main_option == "read_index":
            read_index("read")

      # 3. Commands
      elif user_read_mode_main_option == "-prior" or user_read_mode_main_option == "-home" or user_read_mode_main_option == "-end" or user_read_mode_main_option == "-full":
            start_decision.command_prompting("write","implicit", user_read_mode_main_option)

      # 4. Error handling
      else:
            start_decision.errors(1, user_read_mode_main_option)


def greetings():


      """
      
      Describe: This function is the entry point for the read mode. 
      It prompts the user to select an option to read the database.
      The user can read the full database, read by categories, read by conditions, or read by index.
      The user can also use the command prompt to navigate to other modes. 
      The function returns the user's input to the main function.
      
      """

      # 0. Header and display
      os.system("clear")
      start_decision.header("homepage/read/")
      
      # 1. Options
      print("\n\n Options: ")
      print("-"*30)
      print("1. Read full database")
      print("2. Read by categories")
      print("3. Read by conditions")
      print("4. Read by index (only records)")
      print("-"*30)

      # 2. User input
      print("\n(*) Select your option here: ")
      user_input = str(input("==>  ")).lower()


      # 3. User input handling - no commands
      if user_input == "1" or user_input == "read full database" or user_input == "real full db" or user_input == "full db":
            user_input = "read_complete_db"
      elif user_input == "2" or user_input == "read by categories":
            user_input = "read_categories"
      elif user_input == "3" or user_input == "read by conditions":
            user_input = "read_conditions"
      elif user_input == "4" or user_input == "read by index":
            user_input = "read_index"

      # 4. User input handling - commands
      elif user_input == "-prior":
            user_input = "-prior"
      elif user_input == "-home":
            user_input = "-home"
      elif  user_input == "-end":
            user_input = "-end"
      elif user_input == "-full":
            user_input = "-full"
      

      return user_input
      


def read_complete_db():

      """
      
      Describe: display the database loaded in the homepage function.
      
      """

      # 0. Header and display
      os.system("clear")
      start_decision.header("homepage/read/full_database")

      # 1. Display the database
      print(" - " * 50)
      print(load_csv.df)
      print(f"\nTotal records: {len(load_csv.df)}")
      print(" - " * 50)

      # 2. Command prompt
      start_decision.command_prompting("read", 1)


def read_categories():

      """
      
      Describe: this function allows the user to read the database by categories (columwise).
      
      """

      # 0. Header and display
      os.system("clear")
      start_decision.header("homepage/read/categories")

      # 1. Display the available columns
      print("\n\n\nThe dataset has the following columns: ")
      print("-"*40)
      columns = (load_csv.df.columns.tolist())
      print(columns)
      print("-"*40)

      # 2. User input
      print("\n\n(*) Select your option to read (e.g. views, author, year): ")
      user_input = str(input("==> "))

      # 3. User input handling
      if user_input == "-end" or user_input == "-home" or user_input == "-prior" or user_input == "-full":
            start_decision.command_prompting("write","implicit", user_input)
      else:
            # If the user input is not in the columns, display an error message and try again
            if user_input not in columns:
                  start_decision.errors(2, user_input)
                  read_categories()
            else:
                  # Separate user's columns into a list
                  input_to_list = [item.strip().lower() for item in user_input.split(',')]

                  # Call the filter_by_categories function with the user's columns
                  filter_by_categories(input_to_list)



def filter_by_categories(user_columns : list):


      """
      
      Describe: after input handling, this function filters the database by the user's columns.
      
      """

      # 0. Header and display
      os.system("clear")
      start_decision.header(f"homepage/read_db/categories/selected_columns")
     
      # 1. Display the selected columns
      print(" - " * 30)      
      print(load_csv.df[user_columns])
      print(" - " * 30)

      # 2. Command prompt
      start_decision.command_prompting("read", 2)
     

def read_conditions(mode = None):

      """
      
      Describe: this function allows the user to filter the records. THIS FUNCTION IS NOT POWERED BY REGEX -- TO BE DEVELOPED SOON
      Parameters: 
            - mode: the mode of the session (read, edit_record, delete_record)

      """
      
      # 0. Header and display
      os.system("clear")
      start_decision.header("homepage/read_db/conditions")

      # 1. User input
      print("\n(*) Filter by conditions (e.g: (load_csv.df['title'] == 'one dance') & (load_csv.df['year'] == 2016)  ") # This is going to be difficult to solve more cleanly
      user_input = str(input("==>  "))
      
      # 2. User input handling
      if user_input == "-end" or user_input == "-home" or user_input == "-prior" or user_input == "-full":
            start_decision.command_prompting("write","back_to_greetings", user_input)
      else:
            # Create a code string to filter the records
            prefix= 'dt = load_csv.df['
            postfix = ']'
            code_string = prefix + user_input + postfix

            filter_read_conditions(code_string, mode)

      

def filter_read_conditions(code_string, mode):
    
    """
    
    Describe: this function filters the records by the user's input.

    Parameters:
      - code_string: the code string to be executed
      - mode: the mode of the session (read, edit_record, delete_record)
    
    
    """
    

    # 0. Header and display
    os.system("clear")
    start_decision.header("homepage/read_db/conditions/selected_conditions")

    # 1. Execute the code string  
    locals = {}
    exec(code_string, globals(), locals)

    dt = locals['dt']
    
    # 2. Display the results
    print("\n\nResults of your query: ")
    print("-"*100)
    print(dt)
    print(f"\nTotal records: {len(dt)}")
    print("-"*100)

    # 3. Command prompt
    if mode == "read":
            start_decision.command_prompting("read", 2)
    elif mode == "edit_record":
         print("YOU CURRENTLY CANNOT EDIT RECORDS BY CONDITIONS")
         time.sleep(2)
    elif mode == "delete_record":
         
         df = df.drop(dt.index)

         # Save the new dataframe with the deleted record
         with open(load_csv.url, 'w') as f:
            df.to_csv(f, index = False, header = True)
         


def read_index(mode = None):
    

    """
    
      Describe: this function allows the user to read the records by index or slice.
      Parameters:
            - mode: the mode of the session (read, edit_record, delete_record)
    
    """  

    # 0. Header and display
    os.system("clear")
    start_decision.header("homepage/read/index")


    #1. Display the first 5 records of the database to assist selection
    print("First 5 records of the database: ")
    print(" - " *30)
    print(load_csv.df.head(5))
    print(" - " *30)
    print("\n")

    # 2. Branch user input based on session's mode (READ)
    if mode == "read":
        
        # 1. Select type of subscripting
        print("(*) Select subscripting approach: index (1) or slice (2)")
        selection_mode = input("==>  ").lower()

        # 2. By index    
        if selection_mode == "1" or selection_mode == "index":
           
            print("\n(*) Select index: ")
            index = int(input("==>  "))

            read_index_selected(index)

       # 3. By slice         
        elif selection_mode == "2" or selection_mode == "slice":
            
            print("\n(*) Select slice:")
            lower_bound = (input("Lower bound ==>  "))

            if lower_bound == "-end" or lower_bound == "-home" or lower_bound == "-prior" or lower_bound == "-full":
                  start_decision.command_prompting("write","back_to_greetings", lower_bound)

            elif lower_bound != "-end" or lower_bound != "-home" or lower_bound != "-prior" or lower_bound != "-full":
                  upper_bound = (input("Upper bound ==>  "))

                  if upper_bound == "-end" or upper_bound == "-home" or upper_bound == "-prior" or upper_bound == "-full":
                        start_decision.command_prompting("write","back_to_greetings", (lower_bound,upper_bound))

                  else:
                        read_index_slice(int(lower_bound),int(upper_bound))
                        start_decision.command_prompting("read", 2)

        # 4. Command prompt          
        elif selection_mode == "-end" or selection_mode == "-home" or selection_mode == "-prior" or selection_mode == "-full":
            start_decision.command_prompting("write","back_to_subscripting", selection_mode)
        else:
            # 5. Error handling
            start_decision.errors(1, selection_mode)
            read_index("read")
                 
      # 2. Branch user input based on session's mode (EDIT)
    elif mode == "edit_record":

      print("(*) Select subscripting approach: index (1) or slice (2)")
      selection_mode = input("==>  ").lower()

      if selection_mode == "1" or selection_mode == "index" or selection_mode == "ind":
        print("\n(*) Select index: ")
        index = (input("==>  "))

        if index == "-end" or index == "-home" or index == "-prior" or index == "-full":
                  start_decision.command_prompting("write","back_to_greetings", index)
        else:  
            write_mode.edit_record(int(index))
        
      elif selection_mode == "2" or selection_mode == "slice":

            print("\n(*) Select slice: ")
            lower_bound = (input("Lower bound ==>  "))

            if lower_bound == "-end" or lower_bound == "-home" or lower_bound == "-prior" or lower_bound == "-full":
                  start_decision.command_prompting("write","back_to_greetings", lower_bound)

            elif lower_bound != "-end" or lower_bound != "-home" or lower_bound != "-prior" or lower_bound != "-full":
                  upper_bound = (input("Upper bound ==>  "))

                  if lower_bound == "-end" or upper_bound == "-end" or lower_bound == "-home" or upper_bound == "-home" or lower_bound == "-prior" or upper_bound == "-prior" or lower_bound == "-full" or upper_bound == "-full":
                        start_decision.command_prompting("write","back_to_greetings", lower_bound)
                  else:
                        write_mode.edit_record(int(lower_bound),int(upper_bound))

      # 3. Command prompt
      elif selection_mode == "-prior" or selection_mode == "-home" or selection_mode == "-end" or selection_mode == "-full":
            start_decision.command_prompting("write","back_to_greetings", selection_mode)

      # 4. Error handling
      else:
            start_decision.errors(1, selection_mode)
            read_index("edit_record")
      
    # 2. Branch user input based on session's mode (DELETE)  
    elif mode == "delete_record":

      print("(*) Select subscripting approach: index (1) or slice (2)")
      selection_mode = input("==>  ").lower()

      if selection_mode == "1" or selection_mode == "index" or selection_mode == "ind":
        
        print("\n(*) Select index:")
        index = int(input("==>  "))
        try:
            write_mode.delete_record_index(index)
        except:
            start_decision.errors(3, index)
            read_index("delete_record")
        
      elif selection_mode == "2" or selection_mode == "slice":
            print("\n(*) Select slice")

            lower_bound = (input("Lower bound ==>  "))
            if lower_bound == "-end" or lower_bound == "-home" or lower_bound == "-prior" or lower_bound == "-full":
                  start_decision.command_prompting("write","back_to_greetings", lower_bound)
                  
            elif lower_bound != "-end" or lower_bound != "-home" or lower_bound != "-prior" or lower_bound != "-full":      
                  upper_bound = (input("Upper bound ==>  "))
                  if upper_bound == "-end" or upper_bound == "-home" or upper_bound == "-prior" or upper_bound == "-full":
                        start_decision.command_prompting("write","back_to_greetings", (lower_bound,upper_bound))

                  else:
                        try:
                              write_mode.delete_record_index(int(lower_bound),int(upper_bound))
                        except:
                              start_decision.errors(3, (lower_bound, upper_bound))
                              read_index("delete_record")

      elif selection_mode == "-end" or selection_mode == "-home" or selection_mode == "-prior" or selection_mode == "-full":
            start_decision.command_prompting("write","back_to_greetings", selection_mode)
      else:
            start_decision.errors(1, selection_mode)
            read_index("delete_record")
            
      


def read_index_selected(index):
    

    """
    
    Describe: this function reads the record selected by the user. Called by the read_index function in read mode after INDEX is selected by the user.
    Parameters:
      - index: the index selected by the user
    
    """
    

    # 0. Header and display
    os.system("clear")
    start_decision.header("homepage/read/index/selected_index")

    # 1. Display the record selected  
    print("\n\nRecord selected: ")
    print(load_csv.df.loc[index])

    # 2. Command prompt
    start_decision.command_prompting("read", 2)


def read_index_slice(lower_bound, upper_bound):
    
    """
    
    Describe: this function reads the record selected by the user. Called by the read_index function in read mode after SLICE is selected by the user.
    Parameters:
      - lower_bound: the lower bound index selected by the user
      - upper_bound: the upper bound index selected by the user
    
    """  


    # 0. Header and display
    os.system("clear")
    start_decision.header("homepage/read/index/selected_slice")

    # 1. Display the records selected
    print("\n\nRecords selected: ")
    print(load_csv.df[int(lower_bound):int(upper_bound)])
 
    # 2. Command prompt 
    start_decision.command_prompting("read", 2)
