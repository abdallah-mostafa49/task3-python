#1- write 2 programs that removes duplicates from a list → list = [1,2,3,4,1,5,2,3,6]

#Remove duplicates using set
list1 = [1, 2, 3, 4, 1, 5, 2, 3, 6]
list_without_duplicates = list(set(list1))
print(list_without_duplicates)

#2- write a program that takes phone number from a user and prints it in words. Hint: you should use dictionaries
#input→ Phone : 1234
#output → one two three four


# Program: Convert phone number to words

numbers = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

phone = input("Phone: ")

for digit in phone:
    print(numbers[digit], end=' ')
