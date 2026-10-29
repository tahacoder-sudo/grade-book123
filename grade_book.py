# grade_book.py
# A simple command-line grade book.
students = {}  # name -> list of marks


def calculate_grade(average):
  if average >= 85:
    return "A"
  elif average >= 70:
    return "B"
  elif average >= 55:
    return "C"
  elif average >= 40:
    return "D"
  return "F"


def show_grades():
  if not students:
    print("No students yet.")
    return
  for name, marks in students.items():
    average = sum(marks) / len(marks)
    print(f"{name}: average {average:.1f}, grade {calculate_grade(average)}")


def show_menu():
  print("\n=== Grade Book ===")
  print("1. Show grades")
  print("0. Exit")


def main():
  while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "0":
      print("Goodbye!")
      break
    elif choice == "1":
      show_grades()
    else:
      print("Invalid option.")


if __name__ == "__main__":
  main()
```[cite: 4, 7, 8]