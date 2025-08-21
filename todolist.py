import csv

class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"نام: {self.name} | توضیحات: {self.description} | اولویت: {self.priority}"

class ToDoList:
    def __init__(self, filename="tasks.csv"):
        self.tasks = []
        self.filename = filename
        self.load_from_csv()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_to_csv()

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                self.save_to_csv()
                print(f" کار '{task_name}' حذف شد.")
                return
        print(" کار مورد نظر یافت نشد.")

    def show_tasks(self):
        if not self.tasks:
            print(" لیست کارها خالی است.")
        else:
            print("\n لیست کارها:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def save_to_csv(self):
        with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["نام", "توضیحات", "اولویت"])
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority])

    def load_from_csv(self):
        try:
            with open(self.filename, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(row["نام"], row["توضیحات"], row["اولویت"])
                    self.tasks.append(task)
        except FileNotFoundError:
            pass


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- منوی مدیریت لیست کارها ---")
        print("1. اضافه کردن کار جدید")
        print("2. حذف کار")
        print("3. مشاهده کارها")
        print("4. خروج")

        choice = input("انتخاب شما: ")

        if choice == "1":
            name = input("نام کار: ")
            description = input("توضیحات: ")
            priority = input("اولویت (بالا/متوسط/پایین): ")
            task = Task(name, description, priority)
            todo_list.add_task(task)
            print(" کار اضافه شد.")

        elif choice == "2":
            task_name = input("نام کار برای حذف: ")
            todo_list.remove_task(task_name)

        elif choice == "3":
            todo_list.show_tasks()

        elif choice == "4":
            print(" خداحافظ!")
            break

        else:
            print(" انتخاب نامعتبر، دوباره تلاش کنید.")


if __name__ == "__main__":
    main()