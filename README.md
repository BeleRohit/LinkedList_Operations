# Linked List Operations GUI Project

This project is a Python-based graphical user interface (GUI) application that allows users to perform various linked list operations, including inserting, deleting, searching, and displaying elements of a linked list. The application is built using the `Tkinter` library and implements a modular approach to separate the linked list logic, GUI interface, and logging/error handling.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [Logging](#logging)
- [Error Handling](#error-handling)
- [File Structure](#file-structure)
- [Future Improvements](#future-improvements)

## Features
- **Insert at the Beginning**: Insert a node at the start of the linked list.
- **Insert at the End**: Append a node to the end of the linked list.
- **Insert at a Specific Position**: Insert a node at a given position in the linked list.
- **Delete from the Beginning**: Remove the first node of the linked list.
- **Delete from the End**: Remove the last node of the linked list.
- **Delete from a Specific Position**: Delete a node at a specified position.
- **Search**: Search for a specific value in the linked list.
- **Display**: Display the current linked list.

## Technologies Used
- **Python**: Main programming language.
- **Tkinter**: Used for creating the GUI.
- **Logging**: For tracking application events and errors.

## Prerequisites
- Python 3.x installed on your system.
- Basic knowledge of how to run Python scripts.

## Setup Instructions
1. **Clone the repository** (if available on a platform like GitHub):
    ```bash
    git clone https://github.com/BeleRohit/LinkedList_Operations.git
    ```
2. **Install Tkinter**: Tkinter usually comes pre-installed with Python, but if not, you can install it:
    ```bash
    sudo apt-get install python3-tk
    ```
    For Windows users, Tkinter should be included by default in Python installations.

3. **Install required dependencies**: If any additional dependencies are required, you can install them using:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the project files** if you’re not using version control. The files required are:
    - `linkedlist.py`: Contains the linked list implementation.
    - `gui.py` or main script: The main file for running the Tkinter GUI.

## Running the Project
1. **Run the main Python script** to launch the GUI:
    ```bash
    python gui.py
    ```
    This will open a GUI window where you can interact with the linked list using various operations.

2. **Input Fields**:
    - **Data Entry**: Enter the value you want to insert, search, or delete.
    - **Position Entry**: Enter the position (if required) for insertion or deletion.
  
3. **Operations**: Click the corresponding button to perform an operation:
    - Insert at the Beginning
    - Insert at the End
    - Insert at Position
    - Delete from Beginning
    - Delete from End
    - Delete from Position
    - Search
    - Display

4. **Results**: The result of the operations will be displayed on the GUI itself.

## Logging
All operations, errors, and user actions are logged in a `linkedlist.log` file located in the project directory. This file captures the following:
- Information on successful operations like insertions, deletions, searches.
- Warnings for actions like attempting to delete from an empty list.
- Errors for invalid inputs or unexpected behavior.

## Error Handling
- Invalid input entries (like entering a non-integer value where an integer is expected) are handled by displaying error messages using `messagebox.showerror()`.
- Logging is done for exceptions encountered during linked list operations.
- Boundary checks for positions in the list (e.g., inserting or deleting at a non-existent position) are handled with appropriate error messages.

Feel free to contribute to this project or suggest improvements!

