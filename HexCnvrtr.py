#Jhon Patrick Tacio
#SIA 

def hexCnvrtr(hexNum):
    if hexNum == "0": return "0000"
    elif hexNum == "1": return "0001"
    elif hexNum == "2": return "0010"
    elif hexNum == "3": return "0011"
    elif hexNum == "4": return "0100"
    elif hexNum == "5": return "0101"
    elif hexNum == "6": return "0110"
    elif hexNum == "7": return "0111"
    elif hexNum == "8": return "1000"
    elif hexNum == "9": return "1001"
    elif hexNum == "A": return "1010"
    elif hexNum == "B": return "1011"
    elif hexNum == "C": return "1100"
    elif hexNum == "D": return "1101"
    elif hexNum == "E": return "1110"
    elif hexNum == "F": return "1111"
    else: return "Invalid"
    
hexNum = input("Enter hex numbers separated by space: ").upper().split()

print("\nResults:")
for hexDigit in hexNum:
    result = ""
    for ch in hexDigit:
        result += hexCnvrtr(ch)
    print(hexDigit, "->", result)
