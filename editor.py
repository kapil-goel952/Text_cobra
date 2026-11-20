class PyTextEditor:

    def __init__(self):
        self.lines = []

    # 1. Write text
    def write(self):
        print("\nEnter your text.")
        print("Type :q on a new line to finish.\n")

        while True:
            line = input()

            if line == ":q":
                break

            self.lines.append(line)

        print("\nText added successfully.\n")

    # 2. Read document
    def read(self):
        if not self.lines:
            print("\nDocument is empty.\n")
            return

        print("\n---------- DOCUMENT ----------")

        for number, line in enumerate(self.lines, 1):
            print(f"{number}: {line}")

        print("------------------------------\n")

    # 3. Search text
 def search(self):
        if not self.lines:
            print("\nDocument is empty.\n")
            return

        value = input("\nEnter text to search: ").lower()
        found = False

        for number, line in enumerate(self.lines, 1):
            if value in line.lower():
                print(f"Line {number}: {line}")
                found = True

        if not found:
            print("Text not found.")

        print()

    # 4. Edit line
    def edit_line(self):
        if not self.lines:
            print("\nDocument is empty.\n")
            return

        self.read()

        try:
            number = int(input("Enter line number to edit: "))

            if not 1 <= number <= len(self.lines):
                print("Invalid line number.\n")
                return

            self.lines[number - 1] = input("Enter new text: ")
            print("Line updated successfully.\n")

        except ValueError:
            print("Enter a valid line number.\n")

    # 5. Delete line
    def delete_line(self):
        if not self.lines:
            print("\nDocument is empty.\n")
            return

        self.read()

        try:
            number = int(input("Enter line number to delete: "))

            if not 1 <= number <= len(self.lines):
                print("Invalid line number.\n")
                return

            deleted = self.lines.pop(number - 1)

            print(f"Deleted: {deleted}")
            print("Line deleted successfully.\n")

        except ValueError:
            print("Enter a valid line number.\n")

    # 6. Clear document
    def clear_document(self):
        if not self.lines:
            print("\nDocument is already empty.\n")
            return

        confirm = input("Clear entire document? (y/n): ")

        if confirm.lower() == "y":
            self.lines.clear()
            print("Document cleared successfully.\n")
        else:
            print("Operation cancelled.\n")

    # 7. Save file


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
