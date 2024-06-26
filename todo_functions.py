import csv


def add_todo(file_name):
    todo_name = input("Enter a todo item: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "Not done"])



def remove_todo(file_name):
    todo_name = input("Enter the todo name that you want to delete: ")
    #create a new list
    todo_lists = []
    # Put all the previous items into the list except the one they want to delete
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        is_exist = False
        for row in reader: # [do grecery,False]
            if (todo_name != row[0]):# do laundry != do grocery -> True
                todo_lists.append(row) # [[title,completed], [do grocery,False], [make sandwich,False]]
            else:
                is_exist = True
    if not is_exist:
        print("No item with that name exists.")
    # Write the enter list.csv file with this new list
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)


def mark_todo(file_name):
    todo_name = input("Enter the todo name that you want to mark as complete: ")
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if(todo_name != row[0]):
                todo_lists.append(row)
            else:
                todo_lists.append([row[0], "Done"])

    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)



def View_todo(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            if (row[1] == "Done"):
                print(f"{row[0]} is completed")
            else:
                print(f"{row[0]} is not completed")
    
    
    