from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():  
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:    
        tasks.append(task_string)   
        the_cursor.execute('insert into tasks values (?)', (task_string ,))    
        list_update()    
        task_field.delete(0, 'end')  

def list_update():    
    clear_list()    
    for task in tasks:    
        task_listbox.insert('end', task)  

def delete_task():  
    try:  
        the_value = task_listbox.get(task_listbox.curselection())    
        if the_value in tasks:  
            tasks.remove(the_value)    
            list_update()   
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:   
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        

def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:    
        while(len(tasks) != 0):    
            tasks.pop()    
        the_cursor.execute('delete from tasks')   
        list_update()  

def clear_list():   
    task_listbox.delete(0, 'end')  

def close():    
    print(tasks)   
    guiWindow.destroy()  

def retrieve_database():    
    while(len(tasks) != 0):    
        tasks.pop()    
    for row in the_cursor.execute('select title from tasks'):    
        tasks.append(row[0])  

if __name__ == "__main__":   
    guiWindow = Tk()   
    guiWindow.title("To-Do List ")  
    guiWindow.geometry("665x400+550+250")   
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "white")  

    the_connection = sql.connect('listOfTasks.db')   
    the_cursor = the_connection.cursor()   
    the_cursor.execute('create table if not exists tasks (title text)')  

    tasks = []  

    functions_frame = Frame(guiWindow, bg = "black") 

    functions_frame.pack(side = "top", expand = True, fill = "both")  

    task_label = Label( functions_frame,text = "TO-DO-LIST \n Enter the Task Title:",  
        font = ("arial", "14", "bold"),  
        background = "black", 
        foreground="white"
    )    
    task_label.place(x = 20, y = 30)  

    task_field = Entry(  
        functions_frame,  
        font = ("Arial", "14"),  
        width = 42,  
        foreground="black",
        background = "white",  
    )    
    task_field.place(x = 180, y = 30)  

    add_button =Button(  
        functions_frame,  
        text = "Add",  
        width = 15,
        bg='coral',font=("arial", "14", "bold"),
        command = add_task,

    )  
    del_button = Button(  
        functions_frame,  
        text = "Remove",  
        width = 15,
        bg='coral', font=("arial", "14", "bold"),
        command = delete_task,  
    )  
    del_all_button = Button(  
        functions_frame,  
        text = "Delete All",  
        width = 15,
        font=("arial", "14", "bold"),
        bg='coral',
        command = delete_all_tasks  
    )

    exit_button = Button(  
        functions_frame,  
        text = "Exit / Close",  
        width = 52,
        bg='coral',  font=("arial", "14", "bold"),
        command = close  
    )    
    add_button.place(x = 18, y = 80,)  
    del_button.place(x = 240, y = 80)  
    del_all_button.place(x = 460, y = 80)  
    exit_button.place(x = 17, y = 330)  

    task_listbox = Listbox(  
        functions_frame,  
        width = 70,  
        height = 9,  
        font="bold",
        selectmode = 'SINGLE',  
        background = "gray",
        foreground="white",    
        selectbackground = "white",  
        selectforeground="BLACK"
    )    
    task_listbox.place(x = 17, y = 140)  

    retrieve_database()  
    list_update()    
    guiWindow.mainloop()    
    the_connection.commit()  
    the_cursor.close()

class TaskDatabase:
    def __init__(self, db_name='listOfTasks.db'):
        self.conn = sql.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT, completed INTEGER)')

    def add_task(self, task):
        self.cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (task, 0))
        self.conn.commit()

    def delete_task(self, task):
        self.cursor.execute('DELETE FROM tasks WHERE title = ?', (task,))
        self.conn.commit()

    def delete_all_tasks(self):
        self.cursor.execute('DELETE FROM tasks')
        self.conn.commit()

    def get_tasks(self):
        self.cursor.execute('SELECT title, completed FROM tasks')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

class TaskManager:
    def __init__(self, root):
        self.db = TaskDatabase()
        self.tasks = []

        root.title("To-Do List")
        root.geometry("665x400+550+250")
        root.resizable(0, 0)
        root.configure(bg="white")

        self.functions_frame = Frame(root, bg="black")
        self.functions_frame.pack(side="top", expand=True, fill="both")

        self.create_widgets()
        self.retrieve_database()
        self.update_listbox()

    def create_widgets(self):
        Label(
            self.functions_frame,
            text="TO-DO-LIST \n Enter the Task Title:",
            font=("arial", "14", "bold"),
            bg="black", fg="white"
        ).place(x=20, y=30)

        self.task_field = Entry(
            self.functions_frame,
            font=("Arial", "14"),
            width=42, fg="white", bg="black"
        )
        self.task_field.place(x=180, y=30)

        Button(
            self.functions_frame, text="Add", width=15,
            bg='white', font=("arial", "14", "bold"),
            command=self.add_task
        ).place(x=18, y=80)

        Button(
            self.functions_frame, text="Remove", width=15,
            bg='white', font=("arial", "14", "bold"),
            command=self.delete_task
        ).place(x=240, y=80)

        Button(
            self.functions_frame, text="Delete All", width=15,
            bg='white', font=("arial", "14", "bold"),
            command=self.delete_all_tasks
        ).place(x=460, y=80)

        Button(
            self.functions_frame, text="Exit / Close", width=52,
            bg='white', font=("arial", "14", "bold"),
            command=self.close
        ).place(x=17, y=330)

        self.task_listbox = Listbox(
            self.functions_frame, width=70, height=9,
            font="bold", selectmode='SINGLE',
            bg="black", fg="white",
            selectbackground="white", selectforeground="white"
        )
        self.task_listbox.place(x=17, y=140)

    def add_task(self):
        task = self.task_field.get().strip()
        if not task:
            messagebox.showinfo('Error', 'Field is Empty.')
            return

        if task in self.tasks:
            messagebox.showinfo('Error', 'Task already exists.')
            return

        self.tasks.append(task)
        self.db.add_task(task)
        self.update_listbox()
        self.task_field.delete(0, 'end')

    def delete_task(self):
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            if selected_task in self.tasks:
                self.tasks.remove(selected_task)
                self.db.delete_task(selected_task)
                self.update_listbox()
        except:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def delete_all_tasks(self):
        if messagebox.askyesno('Delete All', 'Are you sure?'):
            self.tasks.clear()
            self.db.delete_all_tasks()
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, 'end')
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def retrieve_database(self):
        self.tasks.clear()
        for task, completed in self.db.get_tasks():
            self.tasks.append(task)

    def close(self):
        self.db.close()
        guiWindow.destroy()

if __name__ == "__main__":
    guiWindow = Tk()
    app = TaskManager(guiWindow)
    guiWindow.mainloop()