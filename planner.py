import json
import os

# A simple file to store tasks permanently
DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_routine():
    print("\n--- Standard Daily Routine ---")
    print("06:30 - 08:00 | Morning Revision / Exercise")
    print("08:30 - 15:30 | Classes & Labs")
    print("16:00 - 18:00 | Sports & Extracurriculars")
    print("19:00 - 21:30 | Deep Work (STEM Focus / Problem Solving)")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== STUDENT PORTAL ===")
        print("1. View Daily Routine")
        print("2. View Study Tasks")
        print("3. Add New Study Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            show_routine()
        elif choice == "2":
            print("\n--- Current Tasks ---")
            if not tasks:
                print("No tasks added yet!")
            for idx, task in enumerate(tasks):
                status = "✓" if task["done"] else " "
                print(f"[{status}] {idx + 1}. {task['title']} ({task['subject']})")
        elif choice == "3":
            title = input("Enter task description: ")
            subject = input("Enter subject (e.g., Physics, Maths): ")
            tasks.append({"title": title, "subject": subject, "done": False})
            save_tasks(tasks)
            print("Task added successfully!")
        elif choice == "4":
            print("Keep working hard! Goodbye.")
            break

if __name__ == "__main__":
    main()