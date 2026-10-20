#Jhon Patrick Tacio
#ClassProg

class PersonInfo:
    def __init__(self):
        self.filename = "C:\\Users\\Admin\\Downloads\\Tacio\\output.txt"
        self.person_info = []

    def readFile(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = file.read()
                print(data if data.strip() != "" else "(empty)")
            print(f"\nFile: {self.filename}")
        except FileNotFoundError:
            print("No file yet - press 1 Add, it will auto-create")

    def writeFile(self, person):
        self.person_info.append(person)
        minor=youth=adult=senior=0
        for p in self.person_info:
            if 0 <= p["age"] <=14: minor+=1
            elif 15 <= p["age"] <=24: youth+=1
            elif 25 <= p["age"] <=64: adult+=1
            else: senior+=1
        with open(self.filename, "w", encoding="utf-8") as file:
            for p in self.person_info:
                file.write(f"{p['name']}, {p['age']}, {p['gender']}\n")
            file.write(f"\nMinor: {minor}\nYouth: {youth}\nAdult: {adult}\nSenior: {senior}\n")
        print(f"Added {person['name']}")
        print(f"Minor: {minor} Youth: {youth} Adult: {adult} Senior: {senior}")
        print(f"File: {self.filename}")

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