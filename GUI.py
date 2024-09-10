import tkinter as tk
from tkinter import messagebox
from linkedlist import LinkedList  # Assuming LinkedList is in a separate file named linkedlist.py

class LinkedListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Linked List Operations")
        self.root.geometry("400x300")

        # Linked list object
        self.ll = LinkedList()

        # Create buttons for operations
        tk.Label(root, text="Linked List Operations").pack()

        self.data_entry = tk.Entry(root)
        self.data_entry.pack()

        self.pos_entry = tk.Entry(root)
        self.pos_entry.pack()

        tk.Button(root, text="Insert at Beginning", command=self.insert_at_beginning).pack()
        tk.Button(root, text="Insert at End", command=self.insert_at_end).pack()
        tk.Button(root, text="Insert at Position", command=self.insert_at_position).pack()
        tk.Button(root, text="Delete from Beginning", command=self.delete_from_beginning).pack()
        tk.Button(root, text="Delete from End", command=self.delete_from_end).pack()
        tk.Button(root, text="Delete from Position", command=self.delete_from_position).pack()
        tk.Button(root, text="Search", command=self.search).pack()
        tk.Button(root, text="Display", command=self.display).pack()

        # Display area
        self.result_label = tk.Label(root, text="", wraplength=300)
        self.result_label.pack()

    def get_data(self):
        try:
            data = int(self.data_entry.get())
            return data
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            return None

    def get_position(self):
        try:
            pos = int(self.pos_entry.get())
            return pos
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            return None

    def insert_at_beginning(self):
        data = self.get_data()
        if data is not None:
            self.ll.insert_at_beginning(data)
            self.result_label.config(text=f"Inserted {data} at the beginning.")

    def insert_at_end(self):
        data = self.get_data()
        if data is not None:
            self.ll.insert_at_end(data)
            self.result_label.config(text=f"Inserted {data} at the end.")

    def insert_at_position(self):
        data = self.get_data()
        pos = self.get_position()
        if data is not None and pos is not None:
            self.ll.insert_at_position(data, pos)
            self.result_label.config(text=f"Inserted {data} at position {pos}.")

    def delete_from_beginning(self):
        result = self.ll.delete_from_beginning()
        self.result_label.config(text=result)

    def delete_from_end(self):
        result = self.ll.delete_from_end()
        self.result_label.config(text=result)

    def delete_from_position(self):
        pos = self.get_position()
        if pos is not None:
            result = self.ll.delete_from_position(pos)
            self.result_label.config(text=result)

    def search(self):
        data = self.get_data()
        if data is not None:
            result = self.ll.search(data)
            self.result_label.config(text=result)

    def display(self):
        elements = self.ll.display()
        self.result_label.config(text=f"List: {elements}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListGUI(root)
    root.mainloop()
