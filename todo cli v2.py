
import json

ACTION_1="Ошибка такого номера нет"
INDEX="Введите индекс:"
DONE="[Выполнено]"

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
        print("Список задач пуст")
        return
    
    for i ,task in enumerate(tasks,start=1):
        status=DONE if task["done"] else "[]"
        print(i ,status,task["text"])

def delete_task(index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index-1)
        print(f"Задача удалена {deleted_task['text']}")
        save_tasks()
    else:
        print(ACTION_1)
def done_task(index):
    if 1 <= index <= len(tasks):
        if tasks[index-1]["done"]:
            print("Задача уже отмечена как выполненная")
            return
        tasks[index-1]["done"]=True
        print(f"Задача отмечена как выполненная {tasks[index-1]['text']}")
        save_tasks()
    else:
        print(ACTION_1)
        
def undone_task(index):
    if 1 <= index <= len(tasks):
        if not tasks[index-1]["done"]:
            print("Задача уже отмечена как невыполненная")
            return
        
        tasks[index-1]["done"]=False
        print(f"Задача отмечена как невыполненная {tasks[index-1]['text']}")
        save_tasks()
    else:
        print(ACTION_1)
        
def edit_task(index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index-1]["text"]=new_task
        save_tasks()
        print("Задача отредактирована")
    else:
        print(ACTION_1)
        
while True:
    user_input=input("add/show/done/undone/delete/edit/exit:").strip()
    parts=user_input.split(maxsplit=1)
    action=parts[0].lower() if parts else ""
    
    if action== "add":
        text = parts[1] if len(parts) > 1 else input("Введите задачу:")
        if text.strip() == "":
            print("Ошибка задача не может быть пустой!") 
            continue
        add_task(text)
        print(f"Задача добавлена {text}")       
    elif action=="show":
        show_tasks()
    elif action=="edit":
        try:
            if len(parts)>1:
                edit_parts=parts[1].split(maxsplit=1)
                index=int(edit_parts[0])
                new_task=edit_parts[1] if len(edit_parts)>1 else input("Введите новую задачу:")
            else:
                index=int(input(INDEX))
                new_task=input("Введите новую задачу:")
            if new_task.strip() == "":
                print("Ошибка задача не может быть пустой!") 
                continue
            edit_task(index, new_task)
        except ValueError:
            print("Ошибка нужно ввести число после edit!")
        except IndexError:
            print("Ошибка нужно ввести индекс и новую задачу после edit!")
        
    elif action == "delete":
        try:
            if len(parts)>1:
                index=int(parts[1])
            else:
                index=int(input(INDEX))
            delete_task(index)
        except ValueError:
            print("Ошибка нужно ввести число после delete!")
    elif action == "done":
        try:
            if len(parts)>1:
                index=int(parts[1])
            else:
                index=int(input(INDEX))
            done_task(index)
        except ValueError:
            print("Ошибка нужно ввести число после done!")
    elif action == "undone":
        try:
            if len(parts)>1:
                index=int(parts[1])
            else:
                index=int(input(INDEX))
            undone_task(index)
        except ValueError:
            print("Ошибка нужно ввести число после undone!")
            
    elif action == "exit":
        print("Выход из программы")
        break
    else:
        print("Неизвестная команда")             