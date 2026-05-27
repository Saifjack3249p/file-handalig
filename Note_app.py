# Task 1 — Notes App

# Features:

# Add notes
# Read notes
# Save into file

def add_note():
    note = input("Enter our notes: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")

def read_notes():
    try:    
        with open("notes.txt", "r") as file:
            notes = file.read()
        print("Your Notes:")
        print(notes)
    except FileNotFoundError:
        print("No notes found.")
