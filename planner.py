import json
import os
import time  # New module to handle the timer countdown

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

def start_pomodoro():
    print("\n=== POMODORO FOCUS TIMER ===")
    try:
        minutes = int(input("Enter study duration in minutes (Standard is 25): "))
    except ValueError:
        print("Invalid input. Defaulting to 25 minutes.")
        minutes = 25
        
    seconds = minutes * 60
    print(f"\nTimer started for {minutes} minutes! Stay focused.")
    print("Press Ctrl + C in the terminal if you need to force-stop early.\n")
    
    # This loop updates the countdown right on the same line
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        # The \r makes the terminal rewrite over the exact same line dynamically
        print(f"Time Remaining: {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
        
    print("\n\n⏱️ TIME IS UP! Splendid session. Take a short break! ⏱️")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== STUDENT PORTAL ===")
        print("1. View Daily Routine")
        print("2. View Study Tasks")
        print("3. Add New Study Task")
        print("4. Mark Task as Done")
        print("5. Start Pomodoro Timer")
        print("6. Delete a Task")
        print("7. Exit")
        
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
            print("\n--- Mark Task as Done ---")
            if not tasks:
                print("No tasks to complete!")
                continue
            for idx, task in enumerate(tasks):
                status = "✓" if task["done"] else " "
                print(f"{idx + 1}. [{status}] {task['title']}")
            
            try:
                task_num = int(input("\nEnter the task number to check off: ")) - 1
                if 0 <= task_num < len(tasks):
                    tasks[task_num]["done"] = True
                    save_tasks(tasks)
                    print(f"Checked off: {tasks[task_num]['title']}! Awesome job.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "5":
            start_pomodoro()
                
        elif choice == "6":
            print("\n--- Delete a Task ---")
            if not tasks:
                print("No tasks to delete!")
                continue
            for idx, task in enumerate(tasks):
                status = "✓" if task["done"] else " "
                print(f"{idx + 1}. [{status}] {task['title']} ({task['subject']})")
            
            try:
                task_num = int(input("\nEnter the task number to delete completely: ")) - 1
                if 0 <= task_num < len(tasks):
                    removed = tasks.pop(task_num)
                    save_tasks(tasks)
                    print(f"Successfully deleted: {removed['title']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "7":
            print("Keep working hard! Goodbye.")
            break

if __name__ == "__main__":
    main()