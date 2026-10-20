# Jhon Patrick Tacio
#Enrollment Program

courseList = [
    "AUTOCAD",
    "TROUBLESHOOTING",
    "PHOTOSHOP",
    "ANIMATION",
    "ROBOTICS"
]

timeSched = [
    "8:00-12:00",
    "12:00-4:00",
    "4:00-8:00"
]

enrollmentSum = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

while True:

    print("\n===== ENROLLMENT PROGRAM =====")
    print("COURSES:")
    print("1 - AUTOCAD")
    print("2 - TROUBLESHOOTING")
    print("3 - PHOTOSHOP")
    print("4 - ANIMATION")
    print("5 - ROBOTICS")

  
    while True:
        try:
            course_choice = int(input("\nYour choice (1-5): "))
            if 1 <= course_choice <= 5:
                break
            else:
                print("Invalid choice. Please choose 1-5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nTIME SCHEDULES:")
    print("1 - 8:00-12:00")
    print("2 - 12:00-4:00")
    print("3 - 4:00-8:00")

  
    while True:
        try:
            time_choice = int(input("\nYour choice (1-3): "))
            if 1 <= time_choice <= 3:
                break
            else:
                print("Invalid choice. Please choose 1-3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    enrollmentSum[course_choice - 1][time_choice - 1] += 1

    while True:
        more = input("\nMore enrollees? (Y/N): ").upper()
        if more == "Y" or more == "N":
            break
        else:
            print("Invalid input. Please enter Y or N.")

    if more == "N":
        break

#Menu
print("\n\n========== ENROLLMENT SUMMARY ==========")

print(f"{'COURSES':<20}", end="")
for schedule in timeSched:
    print(f"{schedule:^15}", end="")
print(f"{'TOTAL':^10}")

print("-" * 75)

#Display 
column_totals = [0, 0, 0]

for i in range(len(courseList)):
    print(f"{courseList[i]:<20}", end="")
    row_total = 0
    for j in range(len(timeSched)):
        print(f"{enrollmentSum[i][j]:^15}", end="")
        row_total += enrollmentSum[i][j]
        column_totals[j] += enrollmentSum[i][j]
    print(f"{row_total:^10}")

print("-" * 75)

#Display
grand_total = sum(column_totals)
print(f"{'TOTALS':<20}", end="")
for total in column_totals:
    print(f"{total:^15}", end="")
print(f"{grand_total:^10}")