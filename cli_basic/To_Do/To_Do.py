import json
import argparse     #subtasks
from pathlib import Path

TASKS=Path("tasks.json")

def load():
    if TASKS.exists():
        with open(TASKS,"r",encoding="utf-8") as f:
            return json.load(f)
    return []
    
def save(tasks):
    with open(TASKS,"w",encoding="utf-8") as f:
        json.dump(tasks,f,indent=2,ensure_ascii=False)

def add(title):
    tasks=load()
    tasks.append({"title":title,"done":False})
    save(tasks)
    print(f"added: {title}")

def list_t():
    tasks=load()
    if not tasks:
        print("List is empty.")
        return
    print("Tasks: ")
    for i, task in enumerate(tasks,start=1):
        status="x" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")

def markdone(index):
    tasks=load()
    try:
        tasks[index-1]["done"]=True
        save(tasks)
        print(f"Accomplished {index}")
    except IndexError:
        print("No tasks")

def remove(index):
    tasks=load()
    try:
        removed=tasks.pop(index-1)
        save(tasks)
        print(f"Deleted {removed['title']}")
    except IndexError:
        print("No tasks")

def main():
    parser=argparse.ArgumentParser(description="CLI To_Do")
    subparsers=parser.add_subparsers(dest="command")

    subparsers.add_parser("list")

    add_p=subparsers.add_parser("add")
    add_p.add_argument("title",type=str)

    done_p=subparsers.add_parser("done")
    done_p.add_argument("index",type=int)

    remove_p=subparsers.add_parser("remove")
    remove_p.add_argument("index",type=int)

    args=parser.parse_args()

    if args.command=="add":
        add(args.title)
    elif args.command=="list":
        list_t()
    elif args.command=="done":
        markdone(args.index)
    elif args.command=="remove":
        remove(args.index)
    else:
        parser.print_help()

if __name__=="__main__":
    main()