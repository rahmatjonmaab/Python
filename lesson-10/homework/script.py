class Task:
    def __init__(self, title, desc, due_date):
        self.title = title
        self.desc = desc
        self.due_date = due_date
        self.done = False

    def mark_complete(self):
        self.done = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all(self):
        for i, task in enumerate(self.tasks):
            status = "✔" if task.done else "✘"
            print(f"{i+1}. {task.title} - {task.due_date} - {status}")

    def list_incomplete(self):
        for i, task in enumerate(self.tasks):
            if not task.done:
                print(f"{i+1}. {task.title} - {task.due_date} - ✘")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

# 🔸 CLI
todo = ToDoList()

while True:
    print("\n1. Add Task\n2. Mark Complete\n3. List All\n4. List Incomplete\n5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        t = input("Title: ")
        d = input("Description: ")
        date = input("Due Date: ")
        todo.add_task(Task(t, d, date))

    elif choice == "2":
        todo.list_all()
        idx = int(input("Task number to mark done: ")) - 1
        todo.mark_done(idx)

    elif choice == "3":
        todo.list_all()

    elif choice == "4":
        todo.list_incomplete()

    elif choice == "5":
        break
      class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for i, post in enumerate(self.posts):
            print(f"{i+1}. {post.title} by {post.author}")

    def posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(f"{post.title} - {post.content}")

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].title = new_title
            self.posts[index].content = new_content

# 🔸 CLI
blog = Blog()

while True:
    print("\n1. Add Post\n2. List All\n3. Posts by Author\n4. Delete\n5. Edit\n6. Exit")
    ch = input("Choose: ")

    if ch == "1":
        t = input("Title: ")
        c = input("Content: ")
        a = input("Author: ")
        blog.add_post(Post(t, c, a))

    elif ch == "2":
        blog.list_posts()

    elif ch == "3":
        a = input("Author name: ")
        blog.posts_by_author(a)

    elif ch == "4":
        blog.list_posts()
        idx = int(input("Post number to delete: ")) - 1
        blog.delete_post(idx)

    elif ch == "5":
        blog.list_posts()
        idx = int(input("Post number to edit: ")) - 1
        new_title = input("New title: ")
        new_content = input("New content: ")
        blog.edit_post(idx, new_title, new_content)

    elif ch == "6":
        break
      class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Not enough balance!")

    def show(self):
        print(f"{self.acc_no} - {self.name} - Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, acc):
        self.accounts.append(acc)

    def find_account(self, acc_no):
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                return acc
        return None

# 🔸 CLI
bank = Bank()

while True:
    print("\n1. Add Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Show Account\n6. Exit")
    ch = input("Choose: ")

    if ch == "1":
        no = input("Account Number: ")
        name = input("Name: ")
        bank.add_account(Account(no, name))

    elif ch == "2":
        no = input("Account Number: ")
        amt = int(input("Amount: "))
        acc = bank.find_account(no)
        if acc:
            acc.deposit(amt)

    elif ch == "3":
        no = input("Account Number: ")
        amt = int(input("Amount: "))
        acc = bank.find_account(no)
        if acc:
            acc.withdraw(amt)

    elif ch == "4":
        from_no = input("From Account: ")
        to_no = input("To Account: ")
        amt = int(input("Amount: "))
        from_acc = bank.find_account(from_no)
        to_acc = bank.find_account(to_no)
        if from_acc and to_acc and from_acc.balance >= amt:
            from_acc.withdraw(amt)
            to_acc.deposit(amt)

    elif ch == "5":
        no = input("Account Number: ")
        acc = bank.find_account(no)
        if acc:
            acc.show()

    elif ch == "6":
        break
