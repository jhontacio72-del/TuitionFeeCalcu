class PersonInfo:
    def __init__(self):
        self.person_info = []
        self.filename = "C:\\Users\\Admin\\Downloads\\Tacio\\output.txt" # use this if you did File > Open Folder > Tacio
        # self.filename = "C:\\Users\\Admin\\Downloads\\Tacio\\output.txt" # use this if you open only Try.py

    def loadFile(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    if "," in line and "Minor:" not in line and "Youth:" not in line and "Adult:" not in line and "Senior:" not in line and line.strip()!= "":
                        parts = line.split(",")
                        if len(parts) == 3:
                            self.person_info.append({
                                "name": parts[0].strip(),
                                "age": int(parts[1].strip()),
                                "gender": parts[2].strip()
                            })
        except FileNotFoundError:
            pass

    def readFile(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = file.read()
                print(data if data.strip()!= "" else "(empty)")

            # COUNT IN VIEW - this is what you asked for
            minor = youth = adult = senior = 0
            for person in self.person_info:
                age = person["age"]
                if 0 <= age <= 14: minor += 1
                elif 15 <= age <= 24: youth += 1
                elif 25 <= age <= 64: adult += 1
                else: senior += 1

            print(f"Minor: {minor}")
            print(f"Youth: {youth}")
            print(f"Adult: {adult}")
            print(f"Senior: {senior}")

            print(f"\nFile link: {self.filename}")

        except FileNotFoundError:
            print("Error: the file could not be found.")

    def writeFile(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            minor = youth = adult = senior = 0
            for person in self.person_info:
                file.write(f"{person['name']}, {person['age']}, {person['gender']}\n")
                age = person["age"]
                if 0 <= age <= 14: minor += 1
                elif 15 <= age <= 24: youth += 1
                elif 25 <= age <= 64: adult += 1
                else: senior += 1
            file.write(f"\nMinor: {minor}\nYouth: {youth}\nAdult: {adult}\nSenior: {senior}\n")
        print(f"Written to {self.filename}")

system = PersonInfo()
system.loadFile()

while True:
    print("\n===== MENU =====")
    print("1 Add")
    print("2 View (the file)")
    print("3 Write (to the file)")
    print("4 Exit")
    c = int(input("Enter (1-4): "))
    if c == 1:
        p = {}
        p["name"] = input("Enter name: ")
        p["age"] = int(input("Enter age: "))
        g = input("Enter gender (F/M): ").lower()
        p["gender"] = "Male" if g == "m" else "Female"
        system.person_info.append(p)
    elif c == 2:
        system.readFile()
    elif c == 3:
        system.writeFile()
    elif c == 4:
        break