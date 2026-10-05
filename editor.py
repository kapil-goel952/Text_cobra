lines = []


def write():
    print("\nEnter your text.")
    print("Type :q on a new line to finish writing.\n")

    while True:
        line = input()

        if line == ":q":
            break

        lines.append(line)

    print("Text added successfully.\n")


def read():
    if not lines:
        print("\nDocument is empty.\n")
        return

    print("\n---------- DOCUMENT ----------")

    for number, line in enumerate(lines, start=1):
        print(f"{number}: {line}")

    print("------------------------------\n")


def search():
    if not lines:
        print("\nDocument is empty.\n")
        return

    value = input("\nEnter the text you want to search for: ")

    found = False

    for number, line in enumerate(lines, start=1):
        if value.lower() in line.lower():
            print(f"Line {number}: {line}")
            found = True

    if not found:
        print("Text not found.")

    print()


def edit_line():
    if not lines:
        print("\nDocument is empty.\n")
        return

    read()

    try:
        number = int(input("Enter the line number you want to edit: "))

        if number < 1 or number > len(lines):
            print("Invalid line number.\n")
            return

        new_text = input("Enter the new text: ")

        lines[number - 1] = new_text

        print("Line updated successfully.\n")

    except ValueError:
        print("Please enter a valid line number.\n")


def delete_line():
    if not lines:
        print("\nDocument is empty.\n")
        return

    read()

    try:
        number = int(input("Enter the line number you want to delete: "))

        if number < 1 or number > len(lines):
            print("Invalid line number.\n")
            return

        deleted = lines.pop(number - 1)

        print(f"Deleted: {deleted}")
        print("Line deleted successfully.\n")

    except ValueError:
        print("Please enter a valid line number.\n")


def clear_document():
    if not lines:
        print("\nDocument is already empty.\n")
        return

    confirm = input("Are you sure you want to clear the document? (y/n): ")

    if confirm.lower() == "y":
        lines.clear()
        print("Document cleared successfully.\n")
    else:
        print("Operation cancelled.\n")


def save_file():
    filename = input("\nEnter filename to save: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")

        print(f"File saved successfully as '{filename}'.\n")

    except OSError as error:
        print(f"Error saving file: {error}\n")


def open_file():
    filename = input("\nEnter filename to open: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines.clear()

            for line in file:
                lines.append(line.rstrip("\n"))

        print(f"File '{filename}' opened successfully.\n")

    except FileNotFoundError:
        print("File not found.\n")

    except OSError as error:
        print(f"Error opening file: {error}\n")


def new_document():
    if lines:
        confirm = input(
            "Current document contains text. "
            "Create a new document anyway? (y/n): "
        )

        if confirm.lower() != "y":
            print("Operation cancelled.\n")
            return

    lines.clear()
    print("New document created.\n")


def menu():
    print("""
========================================
              PY TEXT EDITOR
========================================

1. Write text
2. Read document
3. Search text
4. Edit line
5. Delete line
6. Clear document
7. Save file
8. Open file
9. New document
10. Exit

========================================
""")


while True:
    menu()

    choice = input("Choose an option: ")

    if choice == "1":
        write()

    elif choice == "2":
        read()

    elif choice == "3":
        search()

    elif choice == "4":
        edit_line()

    elif choice == "5":
        delete_line()

    elif choice == "6":
        clear_document()

    elif choice == "7":
        save_file()

    elif choice == "8":
        open_file()

    elif choice == "9":
        new_document()

    elif choice == "10":
        print("\nExiting Py Text Editor...")
        break

    else:
        print("\nInvalid choice. Please choose 1-10.\n")





# l=[]
# def write():
#     print("enter your text :")
#     while True:
#         line=input()
#         if line==":q":
#             break
#         l.append(line)
# def read():
#     for i in l:
#         print(i)
#     return
# def search():
#     val=input("enter the text u wanna search for :")
#     for i in l:
#         if val in i:
#             print("line :",l.index(i)+1," ",i)
#     return

# while True:
#     choice=int(input("""Your Text Editor :\nChoose 1 to enter Text :
#                      Choose 2 to see the text :
#                      Choose 3 to search a word :
#                      choose 4 to exit the editor :"""))
#     match choice:
#         case 1:
#             write()
#         case 2:
#             read()
#         case 3:
#             search()
#         case 4 :
#             exit()