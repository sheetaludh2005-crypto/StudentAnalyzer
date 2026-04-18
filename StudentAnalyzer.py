
marks = []
while True:
    print("\n1. Add Marks")
    print("2. Show Analysis")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        m = int(input("Enter marks: "))
        marks.append(m)

    elif choice == 2:
        if len(marks) == 0:
            print("No data available")
        else:
            total = 0
            for i in marks:
                total = total + i

            avg = total / len(marks)
            highest = max(marks)
            lowest = min(marks)

            print("Total:", total)
            print("Average:", avg)
            print("Highest:", highest)
            print("Lowest:", lowest)

            print("\nGrades and Result:")
            for m in marks:
                if m >= 90:
                    print(m, "- Grade A (Pass)")
                elif m >= 70:
                    print(m, "- Grade B (Pass)")
                elif m >= 40:
                    print(m, "- Grade C (Pass)")
                else:
                    print(m, "- Fail")

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice")