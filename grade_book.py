# grade_book.py
# A simple command-line grade book.
students = {}  # name -> list of marks


def add_student():
  name = input("Student name: ")
  marks = input("Marks separated by spaces: ")
  students[name] = [int(m) for m in marks.split()]
  print(f"Added {name}.")


def show_menu():
  print("\n=== Grade Book ===")
  print("1. Add student")
  print("0. Exit")


def main():
  while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "0":
      print("Goodbye!")
      break
    elif choice == "1":
      add_student()
    else:
      print("Invalid option.")


if __name__ == "__main__":
  main()