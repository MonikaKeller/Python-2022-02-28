def print_employee_data(name: str, age: int, repeat: int = 5, print_line_numbers: bool = False):
    for i in range(0, repeat):
        formatted_data = ""
        if print_line_numbers:
            formatted_data = formatted_data + f"{i + 1} "
        formatted_data = formatted_data + f"{name} {age}"
        print(formatted_data)


print("Begin")
print_employee_data("John Doe", 30, 2, True)
print("Mid")
print_employee_data("Jack Doe", 40, 3)

print_employee_data("Jane Doe", 40)


print_employee_data(age=60, name="John Smith", print_line_numbers=True)

# WARNING
# print_employee_data(100, "Jack Doe")

print("End")
