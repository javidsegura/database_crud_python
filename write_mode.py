
# IMPORTING LIBARRIES
import os,time
import csv, pandas as pd
import numpy as np

# IMPORTING MODULES
import load_csv
import read_mode
import start_decision

def write_main():

      """
      
      Describe: main function for the write mode. It is the entry point for the write mode.
      
      
      """
       
      #1. Set up entry point
      user_write_mode_main_option = greetings()

      # 2. Select modes
      if user_write_mode_main_option == "add":
             colum_or_row("add")

      elif user_write_mode_main_option == "edit":
            colum_or_row("edit")

      elif user_write_mode_main_option == "delete":
            colum_or_row("delete")

      # 3. Commands
      elif user_write_mode_main_option == "-prior" or user_write_mode_main_option=="-home" or  user_write_mode_main_option=="-end" or user_write_mode_main_option=="-full":
            start_decision.command_prompting("write","implicit", user_write_mode_main_option)

      else:
            # 4. Error handling
            start_decision.errors(1, user_write_mode_main_option)



def greetings():


      """
      
      Describe: Displays options within the write mode.
      
      """


      # 0. Header and directory 
      os.system("clear")
      start_decision.header("homepage/write/")
      
      # 1. Options
      print("\n\nOptions: ")
      print("-"*30)
      print("1. Add new record or column")
      print("2. Edit existing record or column")
      print("3. Delete record or column")
      print("-"*30)

      # 2. User input
      print("\n(*) Select your option here: ")
      user_input = str(input("==>  ")).lower()


      # 3. Input handling -- no commands
      if user_input == "1" or   user_input == "add" or user_input == "new":
            user_input = "add"
      elif user_input == "2" or  user_input=="edit":
            user_input = "edit"
      elif user_input == "3" or user_input== "delete" or user_input == "del":
            user_input = "delete"


      # 4. Input handling -- commands
      elif user_input == "-prior":
            user_input = "-prior"
      elif user_input == "-home":
            user_input = "-home"
      elif  user_input == "-end":
            user_input = "-end"
      elif user_input == "-full":
            user_input = "-full"

      return user_input


def colum_or_row(mode = None, axis = None):


      """
      
      Description: second major branch in the write area. It allows the user to select between a row or a column for the chosen mode.
      Parameters:
            - mode: session's mode (add, edit, delete)
            - axis: row or column (used to jump over the selection process)
      
      """


      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write/column_or_row/")

      # 1. User input
      colum_or_row_user_decision = None # Default value when not called from homepage function
      
      if axis == None: 
            print(f"\n(*) Select what you want to {mode}: row (1) or a column (2)?")
            colum_or_row_user_decision = str(input("==>  ")).lower()
      else:
            # If coming from homepage function:
            colum_or_row_user_decision = axis


      # 2. Input handling

      # 2.1. Commands 
      if colum_or_row_user_decision == "-prior" or colum_or_row_user_decision == "-home" or  colum_or_row_user_decision =="-end" or colum_or_row_user_decision =="-full":
            start_decision.command_prompting("write","back_to_greetings", colum_or_row_user_decision)

      #2.2 Row options
      elif colum_or_row_user_decision == "1" or colum_or_row_user_decision == "row" or colum_or_row_user_decision == "record" or colum_or_row_user_decision == "r":

            if mode == "add":
                  add_record()

            elif mode == "edit":
                  print("\n(*) Delete with RegEX search (1) or subscripting (2)?")
                  index_or_conditions = str(input("==> ")).lower()

                  # FUNCTION NOT AVAILABLE YET
                  if index_or_conditions == "1" or  index_or_conditions =="search" or index_or_conditions== "regex":
                        print("FEATURE NOT AVAILABE YET (UNDER DEVELOPMENT)")
                        time.sleep(2)

                  elif index_or_conditions == "2" or index_or_conditions=="subscripting":
                        read_mode.read_index("edit_record") 

            elif mode == "delete":
                  print("\n(*) Delete with RegEX search (1) or subscripting (2)?")
                  index_or_conditions = str(input("==> ")).lower()
                         
                  if index_or_conditions == "1" or  index_or_conditions =="search" or index_or_conditions== "regex":
                       read_mode.read_conditions("delete_record") 

                  elif index_or_conditions == "2" or index_or_conditions=="subscripting":
                        read_mode.read_index("delete_record")

                  #  2.2.3.1. Commands
                  elif index_or_conditions == "-prior" or index_or_conditions=="-home" or index_or_conditions=="-end" or index_or_conditions== "-full":
                        start_decision.command_prompting("write","implicit", index_or_conditions)
                  
            else:
                 # 2.2.4 Error handling
                 start_decision.errors(1, colum_or_row_user_decision)

      # 2.3 Column options
      elif colum_or_row_user_decision == "2" or colum_or_row_user_decision=="column" or colum_or_row_user_decision== "col" or colum_or_row_user_decision== "c":

            if mode == "add":
                  add_column()

            elif mode == "edit":
                  edit_column()

            elif mode == "delete":
                  delete_column()

            else:
                  start_decision.errors(1, colum_or_row_user_decision)


###################
##    ADD MODE   ##
###################


def add_record():

      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write/column_or_row/add/record")

      # 1. Create a new empty row for the new record
      columns = (load_csv.df.columns.tolist())
      new_row = pd.Series(index=columns)
      copy_of_database = pd.DataFrame([new_row])


      flag = True
      print("\nProvide the following information:")
      print("-"*40)

      # 2. Filling all fields for all the columns in the database
      for i in range(len(columns)):

            # 2.1. Display of information
            print(f"Column {i +1}\n", "-"*10)
            print(f"\tColumn name: {columns[i]}")
            print(f"\tData type: {type(load_csv.df.loc[0, columns[i]])}")
            
            # 2.2. User input
            if isinstance(load_csv.df.loc[0,columns[i]], np.int64): # These specific functions should be of type int
                  try:
                        new_value = (input("\t==> "))
                        if new_value == "-home" or new_value == "-prior" or new_value == "-end" or new_value == "-full":
                              flag = False
                              start_decision.command_prompting("write","back_to_greetings", new_value)
                              break
                        else:
                              new_value = np.int64(new_value)
                  except:
                        pass
            else:
                  new_value = str(input("\t==> ")).lower()
                  if new_value == "-home" or new_value == "-prior" or new_value == "-end" or new_value == "-full":
                              flag = False
                              start_decision.command_prompting("write","back_to_greetings", new_value)
                              break
            
            if new_value is not None:
                  copy_of_database.loc[0, columns[i]] = new_value

            print("-"*10)
      print("-"*40)

      if flag == True:
            save_record(copy_of_database)
      

def save_record(copy_of_database):

      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write/column_or_row/add/record/save_record")

      # 1. Confirmation on update
      print("\n(*) Save the following record? (Y or N): ")
      print(copy_of_database.to_string())
      print("-"*40)
      save_record_decision = str(input("\n==>  ")).upper()

      # 2. Confirmed update
      if save_record_decision == "Y":

            # 2.1 Redirect to confirmation page
            os.system("clear")
            start_decision.header("homepage/write/column_or_row/add/record/save_record")
            print("\nStoring record...")

            updated_csv = pd.concat([load_csv.df, copy_of_database], ignore_index=True)

            with open(load_csv.url, 'w') as f:
                  updated_csv.to_csv(f, header=True, index=False)

            os.system("clear")
            start_decision.header("homepage/write/column_or_row/add/record/save_record")
            print("Record saved succesfully.")
            print("-"*30)
            start_decision.command_prompting("read",2)

      # 3. Rejected update
      elif save_record_decision == "N":
            os.system("clear")
            start_decision.header("homepage/write/column_or_row/add/record/save_record")
            print("Record not saved.")
            start_decision.command_prompting("read",2)

      # 4. Commands
      elif save_record_decision == "-home" or save_record_decision == "-prior" or save_record_decision == "-end" or save_record_decision == "-full":
            start_decision.command_prompting("write","implicit", save_record_decision)

      else:  # 5. Error handling
            os.system("clear")
            start_decision.header("homepage/write/column_or_row/add/record/save_record")
            print("Record not saved.")
            start_decision.command_prompting("read",2)



def add_column(): 
      
      """
      
      Describe: add one column (at each call) to the database.
      
      """

      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write/column_or_row/add/column")

      # 1. Information display
      print("\nThe dataset has the following columns: ")
      print("-"*40)
      columns = (load_csv.df.columns.tolist())
      print(columns)
      print("-"*40)

      flag =True

      # 2. User input and input validation
      while flag:

            print("\n(*) Add a new column: ")
            new_column = input("==> ").lower()

            # 2.1 Column already exists
            if new_column in columns:
                  print("Column already exists. Try again.")
                  time.sleep(1)
            
            #2.2 Column does not exist but it is a command
            elif new_column == "-home" or new_column == "-prior" or new_column == "-end" or new_column == "-full":
                  start_decision.command_prompting("write","back_to_greetings", new_column)
                  break

            # 2.3 Column does exist and it is not a command
            else:
                  flag = False
                  save_column(new_column)


def save_column(column_name):

      """
      
      Describe: save the new column to the database.
      Parameters: 
            - column_name: name of the new column.
      
      """

      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write/column_or_row/add/column/save_column")

      # 1. Confirmation on update
      print("\n(*) Save the following column? (Y or N): ")
      load_csv.df[column_name] = None
      print(load_csv.df.to_string())
      print("-"*40)
      save_column_decision = str(input("\n==>  ")).upper()

      # 2. Confirmed update
      if save_column_decision == "Y":
            os.system("clear")

            start_decision.header("homepage/write/column_or_row/add/column/save_column")
            print("\nStoring column...")

            with open(load_csv.url, 'w') as f:
                  load_csv.df.to_csv(f, header=True, index=False)

            os.system("clear")
            start_decision.header("homepage/write/column_or_row/add/column/save_column")
            print("Column saved succesfully.")
            print("-"*30)
            start_decision.command_prompting("read",2)

      # 3. Command
      elif save_column_decision == "-home" or save_column_decision == "-prior" or save_column_decision == "-end" or save_column_decision == "-full":
            start_decision.command_prompting("write","implicit", save_column_decision)

      # 4. Rejected update
      elif save_column_decision == "N":
            os.system("clear")
            start_decision.header("homepage/write/column_or_row/add/column/save_column")
            print("Column not saved.")
            start_decision.command_prompting("read",2)

      # 5. Error handling
      else:
            os.system("clear")
            start_decision.header("homepage/write/column_or_row/add/column/save_column")
            start_decision.errors(1, save_column_decision)
            start_decision.command_prompting("read",2)


###################
##   EDIT MODE   ##
###################

def edit_record(*boundaries):

      """
      
      Describe: edit one or more records in the database. Called in row_index with mode 'edit'
      Parameters: 
            - boundaries: index(ces) of the record to be edited.
      
      """

      # More than one record
      if len(boundaries) > 1:
            lower_bound, upper_bound = boundaries
            edit_record_slice(lower_bound, upper_bound)

      # Only one record      
      else:
            index = boundaries[0]
            edit_record_index(index)

def edit_record_slice(lower_bound, upper_bound):
      
      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write_db/column_or_row/row/edit/slice")
      

      # 1. Display of information
      print("Selected records are: ")
      print("-" * 50)
      print(load_csv.df.loc[int(lower_bound):int(upper_bound)])
      print("-" * 50)
      print("\n\n")

      print("Provide the following information: ")
      print("-" * 50)

      flag = True

      # 2. User input and input validation 
      while lower_bound <= upper_bound and flag: # Looping through the selected records; flag is used to exit the loop from a nested loop
            if lower_bound > upper_bound:
                  break
            print(f"\nEditing record nº {lower_bound}:")
            print("-" *20)
            for i in range(len(load_csv.df.columns)): # For all fields in the given record...
                  column = load_csv.df.columns[i]
                  print(f"\n\t\tColumn: {column}")
                  print(f"\t\tCurrent value: {load_csv.df.loc[int(lower_bound), column]}")
                  if column == "year" or column == "views": # Can be improved with dataype checking 
                        try:
                              new_value = int(input("\t\t==> "))
                        except:
                              pass
                  else:
                        new_value = str(input("\t\t==> ")).lower()

                  if new_value == "-" or new_value == " " or new_value =="" or new_value == None or new_value == "skip":
                        pass

                  elif new_value == "-home" or new_value == "-prior" or new_value == "-end" or new_value == "-full":
                        start_decision.command_prompting("edit","back_to_greetings", new_value)
                        flag = False # Exiting while loop
                        break # Exiting for loop

                  elif new_value != "-" or new_value != " " or new_value !="" or new_value != None or new_value != "skip":
                        load_csv.df.loc[int(lower_bound), column] = new_value
            lower_bound += 1
      print("-" * 50)

      if flag == True: # If no command has been found, proceed to store changes
            edit_record_slice_save()


def edit_record_slice_save():

      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write_db/column_or_row/row/edit/slice/save")

      # 1. Confirmation on update
      print("\n(*) Save the following changes? (Y or N): ")
      print("-"*40)
      print(load_csv.df.to_string())
      print("-"*40)
      save_slice_decision = str(input("\n==>  ")).upper()

      # 2. Confirmed update
      if save_slice_decision == "Y":

            print("\nUpdating the database...")

            with open(load_csv.url, 'w') as f:
                  load_csv.df.to_csv(f, header=True, index=False)

            os.system("clear")
            start_decision.header("homepage/write_db/column_or_row/row/edit/slice/save")
            print("Slice saved succesfully.")
            print("-"*30)
            start_decision.command_prompting("read",2)

      # 3. Commands
      elif save_slice_decision == "-home" or save_slice_decision == "-prior" or save_slice_decision == "-end" or save_slice_decision == "-full":
            start_decision.command_prompting("edit","implicit", save_slice_decision)

      # 4. Rejected update
      elif save_slice_decision == "N":
            os.system("clear")
            start_decision.header("homepage/write_db/column_or_row/row/edit/slice/save")
            print("Updates not saved.")
            start_decision.command_prompting("read",2)

      # 5. Error handling
      else:
            os.system("clear")
            start_decision.header("homepage/write_db/column_or_row/row/edit/slice/save")
            start_decision.errors(1, save_slice_decision)
            start_decision.command_prompting("read",2)


def edit_record_index(user_row):


      """
      
      Describe: 'follow-up' from prior function, but now instead of several records, only one records is edited.
      Parameters:
            - user_row: index of the record to be edited.
      
      """

      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write/column_or_row/row/edit/record/index")
      
      # 1. Display of information
      print("\n\nSelected records are: ")
      print("-" * 50)
      print(load_csv.df.loc[int(user_row)])
      print("-" * 50)

      flag = True # Used to guarantee that only valid edits are proceeded to be saved

      # 2. User input and input validation
      for i in range(len(load_csv.df.columns)): # For all fields in the given (single) record...
                  
                  column = load_csv.df.columns[i]
                  print(f"\n\t\tColumn: {column}")
                  print(f"\t\tCurrent value: {load_csv.df.loc[int(user_row), column]}")

                  if column == "year" or column == "views":
                        try:
                              new_value = int(input("\t\t==> "))
                        except:
                              pass
                  else:
                        new_value = str(input("\t\t==> ")).lower()

                  if new_value == "-" or new_value == " " or new_value =="" or new_value == None or new_value == "skip":
                        pass

                  elif new_value == "-home" or new_value == "-prior" or new_value == "-end" or new_value == "-full":
                        flag = False
                        start_decision.command_prompting("write","back_to_greetings", new_value)
                        break

                  elif new_value != "-" or new_value != " " or new_value !="" or new_value != None or new_value != "skip":
                        load_csv.df.loc[int(user_row), column] = new_value

      if flag == True:
            edit_record_index_save()

def edit_record_index_save():

      """
      
      Describe: save the changes made to the record from edit mode by index.
      
      """

      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write_db/column_or_row/row/edit/record/index/save")

      # 1. Confirmation on update
      print("\n(*) Save the following changes? (Y or N): ")
      print("-"*40)
      print(load_csv.df.to_string())
      print("-"*40)
      save_index_decision = str(input("\n==>  ")).upper()

      # 2. Confirmed update
      if save_index_decision == "Y":
                  print("\nUpdating the database...")
      
                  with open(load_csv.url, 'w') as f:
                        load_csv.df.to_csv(f, header=True, index=False)
      
                  os.system("clear")
                  start_decision.header("homepage/write_db/column_or_row/row/edit/record/index/save")
                  print("Record saved succesfully.")
                  print("-"*30)
                  start_decision.command_prompting("read",2)

      # 3. Commands
      elif save_index_decision == "-home" or save_index_decision == "-prior" or save_index_decision == "-end" or save_index_decision == "-full":
            start_decision.command_prompting("write","implicit", save_index_decision)

      # 4. Rejected update
      elif save_index_decision == "N":
            os.system("clear")
            start_decision.header("homepage/write_db/column_or_row/row/edit/record/index/save")
            print("Record not saved.")
            start_decision.command_prompting("read",2)
      
      # 5. Error handling
      else:
            os.system("clear")
            start_decision.header("homepage/write_db/column_or_row/row/edit/record/index/save")
            start_decision.errors(1, save_index_decision)
            start_decision.command_prompting("read",2)

def edit_column():

      """
      
      Describe: allows to change the name of a column in the database.
      
      """

      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write/column_or_row/column/edit")

      # 1. Display of information
      print("\nThe dataset has the following columns: ")
      print("-"*40)
      columns = (load_csv.df.columns.tolist())
      print(columns)
      print("-"*40)

      # 2. User input and input validation
      print("\n(*) Select the column to edit (separated by commas): ")
      column_to_edit = input("==> ").lower().split(",")
      rename_columns_list = list(column_to_edit)

      # 3. Input validation
      for i in rename_columns_list:
            
            if i == '-home' or i == "-prior" or i == '-end' or i == "-full":
                  start_decision.command_prompting("write","back_to_greetings", i)
                  break 

            if i not in columns:
                  start_decision.errors(2, i)
                  edit_column()
                  
                  
      print()

      # If user input is valid, proceed to rename the columns
      if "-home" not in column_to_edit and "-prior" not in column_to_edit and "-end" not in column_to_edit and "-full" not in column_to_edit:
            for i in rename_columns_list:
                        print("-"*10)
                        new_column_name = input(f"New name for column '{i}': ")
                        load_csv.df.rename(columns={i: new_column_name}, inplace=True)
            # 4. Save changes
            save_edited_column()

def save_edited_column():

      """
      
      Describe: save the changes made to the column's name in the database.
      
      """
      
      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write/column_or_row/column/edit/save")

      # 1. Confirmation on update
      print("\n(*) Save the following changes? (Y or N): ")
      print("-"*40)
      print(load_csv.df.to_string())
      print("-"*40)
      save_column_decision = str(input("\n==>  ")).upper()

      # 2. Confirmed update
      if save_column_decision == "Y":

            print("\nUpdating the database...")

            with open(load_csv.url, 'w') as f:
                  load_csv.df.to_csv(f, header=True, index=False)

            os.system("clear")
            start_decision.header("homepage/write/column_or_row/column/edit/save")
            print("Column saved succesfully.")
            print("-"*30)
            start_decision.command_prompting("read",2)

      # 3. Commands
      elif save_column_decision == "-home" or save_column_decision == "-prior" or save_column_decision == "-end" or save_column_decision == "-full":
            start_decision.command_prompting("write","implicit", save_column_decision)

      # 4. Rejected update
      elif save_column_decision == "N":
            os.system("clear")
            start_decision.header("homepage/write/column_or_row/column/edit/save")
            print("Column not saved.")
            start_decision.command_prompting("read",2)

      # 5. Error handling
      else:
            os.system("clear")
            start_decision.header("homepage/write/column_or_row/column/edit/save")
            start_decision.errors(1, save_column_decision)
            start_decision.command_prompting("read",2)


###################
##  DELETE MODE  ##
###################

def delete_record_index(*boundaries): # delete_record_regex is in filter_read_conditions in module read_mode.py

      """
      
      Describe: delete one or more records in the database. Called in row_index with mode 'delete'
      parameters: 
            - boundaries: index(ces) of the record to be deleted.
      
      """

      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write_db/column_or_row/row/delete/record/save")

      # If subscripting by slice
      if len(boundaries) > 1:
            lower_bound, upper_bound = boundaries
            print("\nYou are about to delete the following records: ")
            print("-"*50)
            print(load_csv.df.loc[int(lower_bound):int(upper_bound)])
            print("-"*50)

      # If subscripting by index
      else:
            index = boundaries[0]
            print("\nYou are about to delete the following record: ")
            print("-"*50)
            print(load_csv.df.loc[int(index)])
            print("-"*50)

      # 1. Confirmation on deletion
      print("\n(*) Confirm deletion? (Y or N): ")
      deletion_index_confirmation = str(input("==>  ")).upper()

      # 2. Confirmed deletion
      if deletion_index_confirmation == "Y":
            if len(boundaries) == 1:
                  updated_df = load_csv.df.drop(load_csv.df.index[int(index)], axis=0)
            else:
                  updated_df = load_csv.df.drop(load_csv.df.index[int(lower_bound):int(upper_bound)], axis=0)

            with open(load_csv.url, 'w') as f:
                  updated_df.to_csv(f, header=True, index=False)
                        
            os.system("clear")
            start_decision.header("homepage/write_db/column_or_row/row/delete/record/save")

            print("Record deleted succesfully.")
            start_decision.command_prompting("read",2)

      # 3. Commands
      elif deletion_index_confirmation == "-home" or deletion_index_confirmation == "-prior" or deletion_index_confirmation == "-end" or deletion_index_confirmation == "-full":
            start_decision.command_prompting("delete","implicit", deletion_index_confirmation)
      
      # 4. Rejected deletion
      elif deletion_index_confirmation == "N":
            os.system("clear")
            start_decision.header("homepage/write_db/column_or_row/row/delete/record/save")
            print("Failed to delete record.")
            start_decision.command_prompting("read",2)

      # 5. Error handling
      else:
            os.system("clear")
            start_decision.header("homepage/write_db/column_or_row/row/delete/record/save")
            start_decision.errors(1, deletion_index_confirmation)
            start_decision.command_prompting("read",2)


            

def delete_column():

      """
      
      Describe: delete one column in the database.
      
      """

      # 0. Header and directory
      os.system("clear")
      start_decision.header("homepage/write_db/column_or_row/column/delete")

      # 1. Display of information
      print("\nThe dataset has the following columns: ")
      print("-"*40)
      columns = (load_csv.df.columns.tolist())
      print(columns)
      print("-"*40)

      # 2. User input and input validation
      print("\n(*) Select the column to delete: ")
      column_to_delete = input("==> ").lower()

      # 3. Commands and input validation
      if column_to_delete == "-home" or column_to_delete == "-prior" or column_to_delete == "-end" or column_to_delete == "-full":
            start_decision.command_prompting("write","back_to_greetings", column_to_delete)

      # 4. Column does not exist 
      elif column_to_delete not in columns:
            start_decision.errors(2, column_to_delete)
            delete_column()
      
      #5. Column exists and is not a command
      else:
            # Eliminate column
            delete_save_changes(column_to_delete)

def delete_save_changes(column_to_delete):

      os.system("clear")
      start_decision.header("homepage/write_db/column_or_row/column/delete/save") 


      load_csv.df.drop(column_to_delete, axis=1, inplace=True)

      # 1. Confirmation on deletion
      print("Database columns: ")
      print("-"*40)
      print(load_csv.df.columns.tolist())
      print("-"*40)

      print("\n(*) Confirm deletion? (Y or N): ")
      deletion_column_confirmation = str(input("==>  ")).upper()

      # 2. Confirmed deletion
      if deletion_column_confirmation == "Y":
            with open(load_csv.url, 'w') as f:
                  load_csv.df.to_csv(f, header=True, index=False)
            os.system("clear")
            start_decision.header("homepage/write_db/column_or_row/column/delete/save")
            print("Column deleted succesfully.")
            start_decision.command_prompting("read",2)
      elif deletion_column_confirmation == "-home" or deletion_column_confirmation == "-prior" or deletion_column_confirmation == "-end" or deletion_column_confirmation == "-full":
            start_decision.command_prompting("write","implicit", deletion_column_confirmation)

      elif deletion_column_confirmation == "N":
            os.system("clear")
            start_decision.header("homepage/write_db/column_or_row/column/delete/save")
            print("Failed to delete column.")
            start_decision.command_prompting("read",2)
      else:
            os.system("clear")
            start_decision.header("homepage/write_db/column_or_row/column/delete/save")
            start_decision.errors(1, deletion_column_confirmation)
            start_decision.command_prompting("read",2)