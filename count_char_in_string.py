'''
    This program takes a String as an input
    and outputs:
        - number of times each character occured
        - number of white spaces
        - handles exceptions(if string is empty/ out of bounds)
'''
import string
def count_all(string_inp):
    if not string_inp:
        print("String is empty")
    total_numbers = {}
    i = 0
    for i in string_inp:
        if i.isalpha():
            if i in total_numbers:
                total_numbers[i] = int(total_numbers[i]) + 1
            else:
                total_numbers[i] = 1
        if i == ' ':
            if i in total_numbers:
                total_numbers[i] = int(total_numbers[i]) + 1
            else:
                total_numbers[i] = 1
        if i in string.punctuation:
            if i in total_numbers:
                total_numbers[i] = int(total_numbers[i]) + 1
            else:
                total_numbers[i] = 1

        if i == "\t":
            if i in total_numbers:
                total_numbers[i] = int(total_numbers[i]) + 1
            else:
                total_numbers[i] = 1
    for j in total_numbers:
        print ("{}:{}".format(j, total_numbers[j]))

if __name__ == '__main__':
    count_all("Hello?!   ")
