
import json

ACTION_1="Error there is no such number"
INDEX="Enter the index:"
DONE="[Done]"

def load_tasks(filename="tasks.json"):
    try:
        with open(filename,"r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks():
    with open("tasks.json","w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

tasks=load_tasks()

def add_task(text):
    tasks.append({"text": text , "done": False})
    save_tasks()
    
def show_tasks():
    if not tasks:
        print("The task list is empty")
        return
    
    for i ,task in enumerate(tasks,start=1):
        status=DONE if task["done"] else "[]"
        print(i ,status,task["text"])

def delete_task(index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index-1)
        print(f"Delete task {deleted_task['text']}")
        save_tasks()
    else:
        print(ACTION_1)
def done_task(index):
    if 1 <= index <= len(tasks):
        if tasks[index-1]["done"]:
            print("The task has already been marked as completed")
            return
        tasks[index-1]["done"]=True
        print(f"The task is marked as completed {tasks[index-1]['text']}")
        save_tasks()
    else:
        print(ACTION_1)
        
def undone_task(index):
    if 1 <= index <= len(tasks):
        if not tasks[index-1]["done"]:
            print("The task has already been marked as unfulfilled ")
            return
        
        tasks[index-1]["done"]=False
        print(f"The task is marked as unfulfilled {tasks[index-1]['text']}")
        save_tasks()
    else:
        print(ACTION_1)
        
def edit_task(index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index-1]["text"]=new_task
        save_tasks()
        print("The issue has been edited")
    else:
        print(ACTION_1)
        
while True:
    user_input=input("add/show/done/undone/delete/edit/exit:").strip()
    parts=user_input.split(maxsplit=1)
    action=parts[0].lower() if parts else ""
    
    if action== "add":
        text = parts[1] if len(parts) > 1 else input("Enter the task:")
        if text.strip() == "":
            print("Error the task cannot be empty!") 
            continue
        add_task(text)
        print(f"Add the task {text}")       
    elif action=="show":
        show_tasks()
    elif action=="edit":
        try:
            if len(parts)>1:
                edit_parts=parts[1].split(maxsplit=1)
                index=int(edit_parts[0])
                new_task=edit_parts[1] if len(edit_parts)>1 else input("Enter a new task:")
            else:
                index=int(input(INDEX))
                new_task=input("Enter a new task:")
            if new_task.strip() == "":
                print("Error the task cannot be empty!") 
                continue
            edit_task(index, new_task)
        except ValueError:
            print("Error you need to enter a number after edit!")
        except IndexError:
            print("Error you need to enter the index and a new task after edit!")
        
    elif action == "delete":
        try:
            if len(parts)>1:
                index=int(parts[1])
            else:
                index=int(input(INDEX))
            delete_task(index)
        except ValueError:
            print("Error you need to enter a number after edit!")
    elif action == "done":
        try:
            if len(parts)>1:
                index=int(parts[1])
            else:
                index=int(input(INDEX))
            done_task(index)
        except ValueError:
            print("Error you need to enter a number after done!")
    elif action == "undone":
        try:
            if len(parts)>1:
                index=int(parts[1])
            else:
                index=int(input(INDEX))
            undone_task(index)
        except ValueError:
            print("Error you need to enter a number after undone!")
            
    elif action == "exit":
        print("Exiting the program")
        break
    else:
        print("Unknown team")             
