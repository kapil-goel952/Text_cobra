
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
    def save_file(self):
        filename = input("\nEnter filename to save: ")

        if not filename.endswith(".txt"):
            filename += ".txt"

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("\n".join(self.lines))

                if self.lines:
                    file.write("\n")

            print(f"File saved successfully as '{filename}'.\n")

        except OSError as error:
            print(f"Error saving file: {error}\n")

    # 8. Open file
    def open_file(self):
        filename = input("\nEnter filename to open: ")

        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            self.lines = content.splitlines()

            print(f"File '{filename}' opened successfully.\n")

        except FileNotFoundError:
            print("File not found.\n")

        except OSError as error:
            print(f"Error opening file: {error}\n")

    # 9. New document
    def new_document(self):
        if self.lines:
            confirm = input(
                "Current document contains text. "
                "Create new document? (y/n): "
            )

            if confirm.lower() != "y":
                print("Operation cancelled.\n")
                return

        self.lines.clear()
        print("New document created.\n")

    # 10. Main menu
    def menu(self):
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

    def run(self):
        while True:
            self.menu()
            choice = input("Choose an option: ")

            match choice:
                case "1":
                    self.write()
                case "2":
                    self.read()
                case "3":
                    self.search()
                case "4":
                    self.edit_line()
                case "5":
                    self.delete_line()
                case "6":
                    self.clear_document()
                case "7":
                    self.save_file()
                case "8":
                    self.open_file()
                case "9":
                    self.new_document()
                case "10":
                    print("\nExiting Py Text Editor...")
                    break
                case _:
                    print("\nInvalid choice. Please choose 1-10.\n")


# Create and run the editor
editor = PyTextEditor()
editor.run()
