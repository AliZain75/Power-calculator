def count_digits(number):
    number_str = str(abs(number)) 
    return len(number_str)
num = int(input("Enter a number: "))
digit_count = count_digits(num)
print(f"The number {num} has {digit_count} digit(s).")