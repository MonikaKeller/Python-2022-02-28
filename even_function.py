def is_even(number: int) -> bool:
    print("calling is_even function")
    # if number % 2 == 0:
    #     return True
    # else:
    #     return False
    return number % 2 == 0


result = is_even(100)
print(result)

print(is_even(101))
