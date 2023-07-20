
# Write a program in Python that takes an integer from user & prints the number of digits it has.
def count_digits(number: int) -> int:
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count
