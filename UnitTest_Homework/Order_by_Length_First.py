def make_grlex(lst):
    return sorted(lst, key=lambda w: (len(w), w))

# lst = []
# n = int(input("Enter number of elements : "))

# for i in range(0, n):
#     message = (input("Enter message : "))
#     lst.append(message) # adding the element
      
# print(make_grlex(lst))