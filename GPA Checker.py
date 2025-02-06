"""
Author: Cierra Danielson
App Name: GPA Checker
Description: This program accepts student names and GPAs, checks if they qualify for
the Dean's List (GPA >= 3.5) or Honor Roll (GPA >= 3.25), and prints a message.
The program terminates when 'ZZZ' is entered as the last name.
"""

def main():
    while True:
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ").strip()
        if last_name.upper() == 'ZZZ':
            print("Exiting program.")
            break

        first_name = input("Enter student's first name: ").strip()
        
        try:
            gpa = float(input("Enter student's GPA: "))
        except ValueError:
            print("Invalid input. Please enter a numeric GPA.")
            continue

        if gpa >= 3.5:
            print(f"Congratulations, {first_name} {last_name}! You have made the Dean's List.")
        elif gpa >= 3.25:
            print(f"Great job, {first_name} {last_name}! You have made the Honor Roll.")
        else:
            print(f"Keep working hard, {first_name} {last_name}! Your GPA is {gpa}.")

if __name__ == "__main__":
    main()