class PersonInfo:
    def __init__(self):
        self.filename = "output.txt"  # No os, just like Sir
        self.person_info = []

    def readFile(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = file.read()
                print(data if data.strip() != "" else "(empty - add a record first)")
            
            # This is the link - in VS Code you Ctrl+Click it
            print(f"\nFile: {self.filename}")
            print("Click the output.txt tab on top - it will open alongside Try.py")

        except FileNotFoundError:
            print("File not found. Right-click Explorer > New File > output.txt")

    def writeFile(self, person):
        self.person_info.append(person)
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(f"{person['name']}, {person['age']}, {person['gender']}\n")
        print("Record added.")
        print(f"Saved to: {self.filename} - check output.txt tab")

system = PersonInfo()

while True:
    print("\n===== MENU =====")
    print("1. Add / Write")
    print("2. Read / View")
    print("3. Exit")
    c = int(input("Enter (1-3): "))
    if c == 1:
        p = {}
        p["name"] = input("Enter name: ")
        p["age"] = int(input("Enter age: "))
        g = input("Enter gender (F/M): ").lower()
        if g == "m": p["gender"] = "Male"
        elif g == "f": p["gender"] = "Female"
        else: p["gender"] = "Unknown"
        system.writeFile(p)
    elif c == 2:
        system.readFile()
    elif c == 3:
        print("Program ended.")
        break
    else:
        print("Invalid choice.")