def calculate_class_allocation():
    num_students = int(input("Enter the number of students: "))
    num_classes = min(2, (num_students + 29) // 30)  # Calculate the minimum number of classes
    class_size = (num_students + num_classes - 1) // num_classes  # Calculate the class size

    allocation = {}
    remaining_students = num_students
    for i in range(1, num_classes + 1):
        students_in_class = min(class_size, remaining_students)
        allocation[f"Class {i}"] = students_in_class
        remaining_students -= students_in_class

    # Print the proposed allocation
    print(f"This is the best way to allocate your students: {num_classes} classes")
    print(allocation)

# Example usage:
calculate_class_allocation()

