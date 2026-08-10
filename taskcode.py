import json
from datetime import datetime
import sys

command = sys.argv[1]

memory = []

try:
    with open('tasks.json', 'r', encoding='utf-8') as file:
        memory = json.load(file)
except FileNotFoundError:
    memory = []

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(memory, f)





if(memory==[]):
    count =1
else:
    count=memory[-1]["ID"]+1

if command == "add":
    description = sys.argv[2]
    
    task = {"ID": count, "description": description, "status": "todo", "createdAt": datetime.now().isoformat(), "updatedAt": datetime.now().isoformat()}
    print(f'Task: "{description}" added with ID {count}')
    memory.append(task)
    count += 1
    save_tasks()
    

elif command == "update":
    id = int(sys.argv[2])
    for task in memory:
        if id==task["ID"]:
            new_description = sys.argv[3]
            print(f'"{task["description"]}" --> "{new_description}"')
            task["description"]=new_description
            task["updatedAt"]= datetime.now().isoformat()
            save_tasks()
            break
    else:
            print("Task with this ID not found")

if command=="delete":
    id = int(sys.argv[2])
    for task in memory:
        if id==task["ID"]:
            memory.remove(task)
            save_tasks()
            print(f"ID {id}: Task deleted")
            break
    else:
            print("Task with this ID not found")

if command=="mark_progress":
    id = int(sys.argv[2])
    for task in memory:
        if id==task["ID"]:
            print(f'Task ID {id}: {task["status"]}-->in-progress')
            task["status"]="in-progress"
            save_tasks()


if command=="mark_done":
    id = int(sys.argv[2])
    for task in memory:
        if id==task["ID"]:
            print(f'Task ID {id}: {task["status"]}-->done')
            task["status"]="done"
            save_tasks()

if command=="list":
    stat = sys.argv[2]
    for task in memory:
        if stat == task["status"]:
            print(task)
