def count_uppercase(lst):
    return sum(1 for word in lst for letter in word if letter.isupper())

# A = input("Enter message : ")

# print(count_uppercase(A))